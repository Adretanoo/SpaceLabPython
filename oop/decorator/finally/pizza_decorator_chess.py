from pizza import Pizza


class PizzaDecoratorChess(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 2

    def description(self):
        return self.pizza.description() + ' з Сиром'

