from animal_factory import AnimalFactory
from polar_bear import PolarBear
from seal import Seal

class ArcticFactory(AnimalFactory):

    def create_hunting(self):
        return PolarBear()
    def create_herbivore(self):
        return Seal()