from user import User
from history import History


user = User("Бодя")
history = History()

print("Поточне ім’я:", user.get_name())
history.backup(user.save())

user.change_name("Саша")
print("Поточне ім’я:", user.get_name())
user.restore(history.undo())

print("ПОпереднє:", user.get_name())

