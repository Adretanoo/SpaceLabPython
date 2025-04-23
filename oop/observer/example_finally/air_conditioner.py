from observer import Observer

class AirConditioner(Observer):
    def update(self, temperature):
        if temperature > 25:
            print("Кондиціонер: Включено, температура більше 25*C.")
        else:
            print("Кондиціонер: Вимкнено, температура менше 25*C.")