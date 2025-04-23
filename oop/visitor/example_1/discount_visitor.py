from visitor import Visitor

class DiscountVisitor(Visitor):
    def visit_book(self, book):
        print(f"Знижка на книгу: {book.price * 0.1}")
        book.price -= book.price * 0.1

    def visit_candy(self, candy):
        print(f"Знижка на цукерки: {candy.price * 0.05}")
        candy.price -= candy.price * 0.05