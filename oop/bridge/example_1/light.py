from abc import ABC, abstractmethod

class Light(ABC):

    @abstractmethod
    def turn_on(self):
        pass
    def off_on(self):
        pass