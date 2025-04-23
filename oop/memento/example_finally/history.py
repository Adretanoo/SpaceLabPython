class History:
    def __init__(self):
        self._history = []

    def backup(self, memento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()
        return ":(("