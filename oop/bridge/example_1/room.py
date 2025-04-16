from led import Led
class Room:

    def __init__(self, light):
        self.light = light

    def turn_on_light(self):
        self.light.turn_on()

    def turn_off_light(self):
        self.light.off_on()

    def avarege_light(self):
        if isinstance(self.light, Led):
            self.light.avarage()
        else:
            print("Цей тип освітлення не підтримує регулювання яскравості.")
