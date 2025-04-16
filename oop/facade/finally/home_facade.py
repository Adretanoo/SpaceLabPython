from light import Light
from temperature_control import TemperatureControl
from security import Security

class SmartHomeFacade:

    def __init__(self):
        self.light = Light()
        self.temperature_control = TemperatureControl()
        self.security = Security()

    def night_mode(self):
        self.light.light_on()
        self.temperature_control.temperature_control_moderate()
        self.security.security_on()

    def morning_mode(self):
        self.light.light_off()
        self.temperature_control.temperature_control_off()
        self.security.security_off()