
class EventFlyweight:

    def __init__(self, name, venue, date):
        self.name = name
        self.venue = venue
        self.date = date

    def display(self, seat_number, price , ticket_id):
        print(f"Квиток + {self.name} , місце проведення {self.venue}, дата {self.date} ID {ticket_id}")