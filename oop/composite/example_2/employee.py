from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def display(self, indent=0):
        pass
