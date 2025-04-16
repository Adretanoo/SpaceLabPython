from ticket import Ticket
from event_factory import EventFactory

factory = EventFactory()

factory = EventFactory()

event1 = factory.get_event("Життя", "Театр", "12-04-2024")
event2 = factory.get_event("Бігуни", "Театр", "12-04-2024")

ticket1 = Ticket("A1", 100, "001", event1)
ticket2 = Ticket("A2", 90, "002", event1)
ticket3 = Ticket("B1", 150, "003", event2)

ticket1.display()
ticket2.display()
ticket3.display()