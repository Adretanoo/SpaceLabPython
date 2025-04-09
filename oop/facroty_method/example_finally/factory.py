from window import Windows
from linux import Linux
from android import Android
from ios import Ios

class OperatingSystemsFactory:

    @staticmethod
    def create_system(name_system):
        name_system = name_system.lower()
        if name_system == 'windows':
            return Windows()
        elif name_system == 'linux':
            return Linux()
        elif name_system == 'android':
            return Android()
        elif name_system == 'ios':
            return Ios()
        else:
            raise ValueError('Error create system')