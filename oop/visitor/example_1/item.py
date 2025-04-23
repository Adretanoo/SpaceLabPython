from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass