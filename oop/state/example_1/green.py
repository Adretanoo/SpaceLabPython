from state import State
from red import Red

class Green(State):
    def handle(self, context):
        print("Зелене світло — ЇДЬ")
        context.set_state(Red())