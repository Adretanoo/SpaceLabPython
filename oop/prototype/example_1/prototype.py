import copy

class Prototype:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        return copy.copy(self)


    def deep_clone(self):
        return copy.deepcopy(self)

# Створюємо об'єкт-прототип
prototype = Prototype("Prototype1", {"key": "value"})

# Копіюємо об'єкт
clone1 = prototype.clone()  # Поверхнева копія
clone2 = prototype.deep_clone()  # Глибока копія

# Виводимо на екран
print(f"Prototype name: {prototype.name}, Data: {prototype.data}")
print(f"Clone1 name: {clone1.name}, Data: {clone1.data}")
print(f"Clone2 name: {clone2.name}, Data: {clone2.data}")

# Змінюємо дані в клонах
clone1.data["key"] = "modified"
clone2.name = "Clone2"

# Перевіряємо зміни
print(f"Prototype after modification: {prototype.name}, Data: {prototype.data}")
print(f"Clone1 after modification: {clone1.name}, Data: {clone1.data}")
print(f"Clone2 after modification: {clone2.name}, Data: {clone2.data}")
