
class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, next_handler):
        self.next = next_handler
        return self

    def handle(self, message):
        if self.next is None:
            return "Не можу обробити це повідомлення."
        return self.next.handle(message)