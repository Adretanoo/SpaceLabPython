class CoffeeMachine:
    def __init__(self, mediator):
        self.mediator = mediator

    def brew_coffee(self):
        print("Вариться кава")