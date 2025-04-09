import copy


class CarPrototype:

    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


    def clone(self):
        return copy.copy(self)

    def deep_copy(self):
        return copy.deepcopy(self)