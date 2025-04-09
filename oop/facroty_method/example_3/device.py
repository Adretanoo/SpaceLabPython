from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def specs(self) -> str:
        pass