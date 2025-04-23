from observer import Observer

class Heater(Observer):
    def update(self, temperature):
        if temperature < 18:
            print("Обігрівач: Включено, температура менше 18*C.")
        else:
            print("Обігрівач: Вимкнено, температура більше 18*C.")
