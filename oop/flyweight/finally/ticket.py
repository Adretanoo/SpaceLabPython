from event_flyweight import EventFlyweight


class Ticket(EventFlyweight):

    def __init__(self, seat, price, ticket_id, event_flyweight : EventFlyweight):
        self.seat = seat
        self.price = price
        self.ticket_id = ticket_id
        self.event_flyweight = event_flyweight


    def display(self):
        self.event_flyweight.display(self.seat, self.price, self.ticket_id)