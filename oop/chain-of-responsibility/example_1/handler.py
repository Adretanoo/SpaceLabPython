class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, message):
        if self.next:
            return self.next.handle(message)
        return "Ніхто не знає, що з цим робити."