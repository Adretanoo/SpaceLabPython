from pizza import Pizza
from pizza_decorator_chess import PizzaDecoratorChess
from pizza_decorator_olives import PizzaDecoratorOlives
from pizza_decorator_mushrooms import PizzaDecoratorMushrooms


pizza = Pizza("Pizza")
print('Ціна ' + str(pizza.cost()))
print(pizza.description() + '\n')


pizza_chess = PizzaDecoratorChess(pizza)
print('Ціна ' + str(pizza_chess.cost()))
print(pizza_chess.description() + '\n')

pizza_olives = PizzaDecoratorOlives(pizza)
print('Ціна ' + str(pizza_olives.cost()))
print(pizza_olives.description() + '\n')

pizza_mushrooms = PizzaDecoratorMushrooms(pizza)
print('Ціна ' + str(pizza_mushrooms.cost()))
print(pizza_mushrooms.description() + '\n')
