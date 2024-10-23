import sqlite3

def print_db_schema(db_path):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")

            # Query to get the schema of the table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            print("Columns:")
            for column in columns:
                print(f"  {column[1]} ({column[2]})")

            print("\n")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Path to your SQLite database
db_path = 'dump.db'
print_db_schema(db_path)