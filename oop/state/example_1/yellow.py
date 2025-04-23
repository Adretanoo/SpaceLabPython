from state import State
from green import Green


class Yellow(State):
    def handle(self, context):
        print("Жовте світло — ГОТУЙСЯ")
        context.set_state(Green())
