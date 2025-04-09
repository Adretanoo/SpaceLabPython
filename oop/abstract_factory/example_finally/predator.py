from abc import ABC, abstractmethod

class Predator(ABC):

    @abstractmethod
    def hunting(self):
        pass