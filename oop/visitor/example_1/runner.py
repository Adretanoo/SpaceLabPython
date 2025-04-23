from book import Book
from candy import Candy
from discount_visitor import DiscountVisitor


book = Book(100)
candy = Candy(50)

discount_visitor = DiscountVisitor()

items = [book, candy]
for item in items:
    item.accept(discount_visitor)

print(f"Нова ціна книги: {book.price}")
print(f"Нова ціна цукерок: {candy.price}")
