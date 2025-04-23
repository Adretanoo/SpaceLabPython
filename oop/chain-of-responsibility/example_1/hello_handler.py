from handler import Handler

class HelloHandler(Handler):
    def handle(self, message):
        if message == "Привіт":
            return "Привіт! Як справи?"
        return super().handle(message)