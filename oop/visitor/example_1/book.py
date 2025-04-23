from item import Item

class Book(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)