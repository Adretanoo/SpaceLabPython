from truck import *
from ship import *


def create_transport(transport_type):
    if transport_type == "road":
        return Truck()
    elif transport_type == "sea":
        return Ship()
    else:
        raise ValueError("Невідомий тип транспорту")


transport = create_transport("sea")
transport.deliver()
