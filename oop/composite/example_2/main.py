from simple_employee import SimpleEmployee
from manager import Manager

em1 = SimpleEmployee('John', 'Робочий станка')
em2 = SimpleEmployee('Vasyl','Прибиральник')
em3 = SimpleEmployee('Anton','Зварювальник')

em4 = SimpleEmployee('Zzz','програміст')

manager_factory = Manager('Завод')
manager_company = Manager('Компанія')


manager_factory.add_subordinate(em1)
manager_factory.add_subordinate(em2)
manager_factory.add_subordinate(em3)

manager_company.add_subordinate(em4)


root = Manager('Начальник')
root.add_subordinate(manager_factory)
root.add_subordinate(manager_company)

root.display()
