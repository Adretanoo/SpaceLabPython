from abc import ABC, abstractmethod

class Herbivore(ABC):
    @abstractmethod
    def eating(self):
        pass