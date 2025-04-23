from handler import Handler

class SpamHandler(Handler):

    def handle(self, message):
        message = message.split(" ")
        for i in range(len(message)):
            if message[i].lower() == "спам":
                return "Повідомлення заблоковано через спам."
        message = " ".join(message)
        return super().handle(message)