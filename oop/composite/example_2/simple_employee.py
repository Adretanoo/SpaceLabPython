from employee import Employee

class SimpleEmployee(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self, indent=0):
        print(" " * indent + f"Працівник {self.name}, {self.position}")