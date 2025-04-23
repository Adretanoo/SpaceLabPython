from yellow import Yellow


class TrafficLight:
    def handle(self, context):
        print("Червоне світло — СТОП")
        context.set_state(Yellow())
