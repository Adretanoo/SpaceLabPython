from mediator import Mediator
from button import Button
from text_box import TextBox


class DialogMediator(Mediator):
    def __init__(self):
        self.button = Button(self)
        self.textbox = TextBox(self)

    def notify(self, sender, event):
        if event == "click":
            if self.textbox.text:
                print("Відправляємо: ", self.textbox.text)
            else:
                print("Поле вводу порожнє!")
        elif event == "text_change":
            print("Текст було змінено.")