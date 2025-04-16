from notifier import Notifier

class TelegramNotifier(Notifier):

    def send(self, to, message):
        print(f"[Telegram] До: {to} | Повідомлення: {message}")