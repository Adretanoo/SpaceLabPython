class Pizza:
    def __init__(self, name):
        self.name = name

    def cost(self):
        return 5

    def description(self):
        return f"Піца: {self.name}"
