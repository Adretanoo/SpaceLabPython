class History:
    def __init__(self):
        self._states = []

    def backup(self, memento):
        self._states.append(memento)

    def undo(self):
        if self._states:
            return self._states.pop()
        return None