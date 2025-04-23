from abc import ABC, abstractmethod

# Абстрактний посередник
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass