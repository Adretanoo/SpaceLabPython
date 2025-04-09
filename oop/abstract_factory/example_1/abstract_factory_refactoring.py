from abc import ABC, abstractmethod

# Абстрактні продукти
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Конкретні продукти
class WindowsButton(Button):
    def render(self) -> str:
        return "Windows Button"

class MacButton(Button):
    def render(self) -> str:
        return "Mac Button"

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Windows Checkbox"

class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Mac Checkbox"

# Абстрактна фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретні фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Клієнтський код
def render_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# Використання
os_type = input("Введіть OS (Windows/Mac): ").strip().lower()
if os_type == "windows":
    factory = WindowsFactory()
elif os_type == "mac":
    factory = MacFactory()
else:
    raise ValueError("Невідома операційна система")

render_gui(factory)
