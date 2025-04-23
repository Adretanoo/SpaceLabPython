from name_memento import NameMemento

class User:
    def __init__(self, name):
        self._name = name

    def change_name(self, new_name):
        print(f"Зміна імені з '{self._name}' на '{new_name}'")
        self._name = new_name

    def get_name(self):
        return self._name

    def save(self):
        return NameMemento(self._name)

    def restore(self, memento):
        self._name = memento.get_name()
        print(f"Ім'я відновлено до: '{self._name}'")