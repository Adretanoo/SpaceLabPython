from abc import ABC, abstractmethod

class UiComponent(ABC):

    @abstractmethod
    def render(self, indent=0):
        pass

    @abstractmethod
    def pour_completely(self):
        pass