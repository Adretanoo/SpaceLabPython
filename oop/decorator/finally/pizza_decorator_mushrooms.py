from pizza import Pizza


class PizzaDecoratorMushrooms(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 1.5

    def description(self):
        return self.pizza.description() + ' з Грибами'
