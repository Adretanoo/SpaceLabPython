from event_flyweight import EventFlyweight


class EventFactory:
    def __init__(self):
        self.events = {}

    def get_event(self, name, venue, date):
        key = (name, venue, date)
        if key not in self.events:
            self.events[key] = EventFlyweight(name, venue, date)
        return self.events[key]
