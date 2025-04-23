from handler import Handler

class DefaultHandler(Handler):
    def handle(self, message):
        return f"Команда '{message}' не розпізнана."