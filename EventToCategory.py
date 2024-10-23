class EventToCategory:
    def __init__(self, index, event_id, event_type, age_restriction, categories):
        self.index = index
        self.event_id = event_id
        self.event_type = event_type
        self.age_restriction = age_restriction
        self.categories = categories

    def to_dict(self):
        return {
            "index": self.index,
            "EventID": self.event_id,
            "Type": self.event_type,
            "AgeRestriction": self.age_restriction,
            "Categories": self.categories
        }