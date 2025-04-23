from item import Item

class Candy(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        visitor.visit_candy(self)