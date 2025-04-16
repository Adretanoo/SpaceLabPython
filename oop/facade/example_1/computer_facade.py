from cpu import CPU
from memory import Memory
from hard_drive import HardDrive


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("Starting computer...")
        self.cpu.process()
        self.memory.load()
        self.hard_drive.read()
        print("Computer started!")