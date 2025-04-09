from africa_factory import AfricaFactory
from artic_factory import ArcticFactory
from animal_factory import AnimalFactory



def render(factory: AnimalFactory):
    hunt = factory.create_hunting()
    herbivore = factory.create_herbivore()
    print(hunt.hunting())
    print(herbivore.eating())


environment_type = input("Введіть середовище (Африка/Артика): ").strip().lower()
if environment_type == "африка":
    factory = AfricaFactory()
elif environment_type == "артика":
    factory = ArcticFactory()
else:
    raise ValueError("Невідоме середовище")

render(factory)