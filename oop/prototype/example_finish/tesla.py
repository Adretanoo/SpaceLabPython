from car import CarPrototype


class Tesla(CarPrototype):
    def __init__(self, model, color, year):
        super().__init__("Tesla", model, color, year)
