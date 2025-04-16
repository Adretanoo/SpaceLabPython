

class MessageDecorator:
    def __init__(self, message):
        self.message = message


    def send(self):
        if self.is_valid():
            print('Message sent.')
        else:
            print('Message is invalid.')

    def is_valid(self):
        return False