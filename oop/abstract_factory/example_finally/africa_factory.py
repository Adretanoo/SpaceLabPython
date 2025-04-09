from animal_factory import AnimalFactory
from lion import Lion
from zebra import Zebra

class AfricaFactory(AnimalFactory):

    def create_hunting(self):
        return Lion()

    def create_herbivore(self):
        return Zebra()