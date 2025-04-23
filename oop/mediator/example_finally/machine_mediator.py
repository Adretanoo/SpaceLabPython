from mediator import Mediator

class MachineMediator(Mediator):
    def __init__(self):
        self.alarm = None
        self.coffee = None

    def set_components(self, alarm, coffee):
        self.alarm = alarm
        self.coffee = coffee

    def notify(self, sender, event):
        if sender is self.alarm and event == "alarm":
            print("Отримано подію 'alarm' — запускаємо кавоварку")
            self.coffee.brew_coffee()