from ui_component import UiComponent


class Label(UiComponent):

    def __init__(self, name):
        self.name = name

    def render(self, indent=0):
        print(' ' * indent + f'Label {self.name}')

    def pour_completely(self):
        print(f'Заливи {self.name} повнісю')
