from temperature_sensor import TemperatureSensor
from air_conditioner import AirConditioner
from heater import Heater


sensor = TemperatureSensor()

ac = AirConditioner()
heater = Heater()

sensor.attach(ac)
sensor.attach(heater)

sensor.set_temperature(30)
sensor.set_temperature(15)
sensor.set_temperature(18)
