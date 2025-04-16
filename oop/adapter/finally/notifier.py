from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, to, message):
        pass