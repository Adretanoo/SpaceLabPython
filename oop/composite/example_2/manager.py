from employee import Employee

class Manager(Employee):

    def __init__(self, employee):
        self.employee = employee
        self.workers = []

    def add_subordinate(self, employee):
        self.workers.append(employee)

    def remove_subordinate(self, employee):
        self.workers.remove(employee)

    def display(self, indent=0):
        print(" " * indent + f" Менеджер: {self.employee}")
        for employee in self.workers:
            employee.display(indent + 2)
