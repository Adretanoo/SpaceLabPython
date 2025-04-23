from light import Light
from turn_on_command import TurnOnCommand
from turn_off_command import TurnOffCommand
from button import Button


light = Light()

turn_on = TurnOnCommand(light)
turn_off = TurnOffCommand(light)

button = Button()


button.set_command(turn_on)
button.press()

button.set_command(turn_off)
button.press()
