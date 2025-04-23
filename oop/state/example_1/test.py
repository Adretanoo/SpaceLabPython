from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class Red(State):
    def handle(self, context):
        print("Червоне світло — СТОП")
        context.set_state(Yellow())


class Yellow(State):
    def handle(self, context):
        print("Жовте світло — ГОТУЙСЯ")
        context.set_state(Green())


class Green(State):
    def handle(self, context):
        print("Зелене світло — ЇДЬ")
        context.set_state(Red())


class TrafficLight:
    def __init__(self):
        self.state = Red()

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle(self)


light = TrafficLight()
light.handle()
light.handle()
light.handle()
light.handle()
