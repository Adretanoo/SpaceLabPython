from handler import Handler

class HelpHandler(Handler):
    def handle(self, message):
        if message == "Допомога":
            return "Ось список команд: ..."
        return super().handle(message)