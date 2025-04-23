class AlarmClock:
    def __init__(self, mediator):
        self.mediator = mediator

    def ring(self):
        print("Будильник кричить")
        self.mediator.notify(self, "alarm")