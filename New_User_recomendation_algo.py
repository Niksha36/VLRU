from flask import Flask, jsonify, request
import sqlite3
import json

from EventToCategory import EventToCategory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Event API. Use /api/events to get event data."

@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        number = request.args.get('number', default=10, type=int)  # Get the number parameter
        page = request.args.get('page', default=1, type=int)  # Get the page parameter

        conn = sqlite3.connect('dump.db')
        cursor = conn.cursor()

        cursor.execute(
        """SELECT
            Event_to_Category.EventID,
            COUNT(UserPath.EventID) AS OccurrenceCount
        FROM
            UserPath
        INNER JOIN
            Event_to_Category ON UserPath.EventID = Event_to_Category.EventID
        GROUP BY
            Event_to_Category.EventID;
        """)

        results = cursor.fetchall()
        data = [row for row in results]
        sorted_data_by_occurrences = sorted(data, key=lambda x: x[1], reverse=True)
        sorted_ids = [sublist[0] for sublist in sorted_data_by_occurrences]

        cursor.execute("SELECT * FROM Event_to_Category")
        Event_to_Category_contents = cursor.fetchall()
        conn.close()
        #Это зачем???
        order_index = {item: index for index, item in enumerate(sorted_data_by_occurrences)}
        sorted_algo_output = []
        for id in sorted_ids:
            num = 0
            for item in Event_to_Category_contents:
                if item[1] == id:
                    sorted_algo_output.append(item)
                    Event_to_Category_contents.pop(num)
                    continue
                num += 1

        for event in Event_to_Category_contents:
            sorted_algo_output.append(event)

        events = [EventToCategory(*event).to_dict() for event in sorted_algo_output]

        # Implement pagination
        start = (page - 1) * number
        end = start + number
        paginated_events = events[start:end]

        return app.response_class(
            response=json.dumps({"events": paginated_events}, ensure_ascii=False),
            mimetype='application/json'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)