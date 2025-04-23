class Button:
    def __init__(self, mediator):
        self.mediator = mediator

    def click(self):
        print("Кнопка натиснута")
        self.mediator.notify(self, "click")