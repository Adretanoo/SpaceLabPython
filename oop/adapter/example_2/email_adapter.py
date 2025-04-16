from message_sender import MessageSender


class EmailAdapter(MessageSender):
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_message(self, to, message):
        self.email_sender.send_email(to, message, check)
