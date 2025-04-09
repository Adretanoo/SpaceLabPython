from abc import ABC, abstractmethod
class AnimalFactory(ABC):

    @abstractmethod
    def create_herbivore(self):
        pass

    @abstractmethod
    def create_hunting(self):
        pass