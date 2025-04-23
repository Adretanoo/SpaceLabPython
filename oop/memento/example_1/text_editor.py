from memento import Memento

class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text

    def get_text(self):
        return self._text

    def save(self):
        return Memento(self._text)

    def restore(self, memento: Memento):
        self._text = memento.get_saved_state()