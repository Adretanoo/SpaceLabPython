from car import CarPrototype


class Car(CarPrototype):
    def __init__(self, model, color, year):
        super().__init__("BMW", model, color, year)
