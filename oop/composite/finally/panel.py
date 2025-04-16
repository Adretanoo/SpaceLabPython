from ui_component import UiComponent


class Panel(UiComponent):

    def __init__(self, element):
        self.element = element
        self.elements = []

    def add(self, component):
        self.elements.append(component)

    def remove(self, component):
        self.elements.remove(component)

    def render(self, indent=0):
        print(' ' * indent + f'Panel {self.element}')
        for element in self.elements:
            element.render(indent + 2)

    def pour_completely(self):
        for element in self.elements:
            element.pour_completely()
        print(f'Заливи {self.element} повнісю')
