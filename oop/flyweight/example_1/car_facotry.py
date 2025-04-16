from car_flyweight import Car

class CarFactory:
    def __init__(self):
        self._cars = {}

    def get_car(self, brand, model, color):
        key = (brand, model, color)
        if key not in self._cars:
            self._cars[key] = Car(brand, model, color)
        return self._cars[key]