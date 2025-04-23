from coffee_template import CoffeeTemplate

class BlackCoffee(CoffeeTemplate):
    def boil_water(self):
        print("Закип'ятити воду.")

    def brew_coffee_grinds(self):
        print("Заварити мелений кофе.")

    def pour_in_cup(self):
        print("Налити каву в чашку.")

    def add_condiments(self):
        print("Не додавати нічого, чорна кава готова!")
