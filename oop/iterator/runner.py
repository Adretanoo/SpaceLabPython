from my_collection import MyCollection

my_collection = MyCollection()
my_collection.add_item("Перше")
my_collection.add_item("Друге")
my_collection.add_item("Третє")

iterator = my_collection.create_iterator()

while iterator.has_next():
    print(iterator.next())