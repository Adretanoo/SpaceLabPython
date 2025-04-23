from handler import Handler


class CensorFilter(Handler):

    def handle(self, message):
        message = message.split(" ")
        for item in range(len(message)):
            if message[item].lower() in ["дурак", "ідіот"]:
                message[item] = "****"
        message = " ".join(message)
        if self.next:
            return self.next.handle(message)
        return message


