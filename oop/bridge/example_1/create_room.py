from lampa import Lampa
from led import Led
from room import Room

lampa = Lampa()
room1 = Room(lampa)
room1.turn_on_light()
room1.turn_off_light()
room1.avarege_light()


led = Led()
room2 = Room(led)
room2.turn_off_light()
room2.turn_off_light()
room2.avarege_light()
