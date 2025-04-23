class Button:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press(self):
        if self.command:
            self.command.execute()
