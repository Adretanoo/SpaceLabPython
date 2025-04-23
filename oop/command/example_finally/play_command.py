class PlayCommand:

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.play()