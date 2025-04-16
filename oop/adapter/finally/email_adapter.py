from notifier import Notifier


class EmailAdapter(Notifier):
    def __init__(self, legacy_email_sender):
        self.legacy_email_sender = legacy_email_sender

    def send(self, to, message):
        self.legacy_email_sender.send_email(to, message)
