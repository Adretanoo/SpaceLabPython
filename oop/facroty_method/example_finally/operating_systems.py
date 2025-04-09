from abc import ABC, abstractmethod

class OperatingSystem(ABC):
    @abstractmethod
    def create_system(self):
        pass