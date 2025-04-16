from ui_component import UiComponent

class Button(UiComponent):

    def __init__(self, name):
        self.name = name

    def render(self, indent=0):
        print(' ' * indent + f'Button {self.name}')

    def pour_completely(self):
        print(f'Заливи {self.name} повнісю')