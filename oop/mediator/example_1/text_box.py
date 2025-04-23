class TextBox:
    def __init__(self, mediator):
        self.mediator = mediator
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Введено текст: {text}")
        self.mediator.notify(self, "text_change")