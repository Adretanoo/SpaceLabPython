from handler import Handler


class ShortFilter(Handler):

    def handle(self, message):
        if len(message) < 2:
            return "Повідомлення занадто коротке!"
        return super().handle(message)
