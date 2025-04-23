from abc import ABC, abstractmethod

class CoffeeTemplate(ABC):
    def make_coffee(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def boil_water(self):
        pass

    @abstractmethod
    def brew_coffee_grinds(self):
        pass

    @abstractmethod
    def pour_in_cup(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass