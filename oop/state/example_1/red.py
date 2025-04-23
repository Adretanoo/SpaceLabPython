from state import State
from yellow import Yellow


class Red(State):
    def handle(self, context):
        print("Червоне світло — СТОП")
        context.set_state(Yellow())
