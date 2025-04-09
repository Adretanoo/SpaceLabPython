from pc import Pc
from laptop import Laptop
from smartphone import Smartphone

class DeviceFactory:

    @staticmethod
    def create_device(device_name) -> str:
        device_name = device_name.lower()
        if device_name == 'pc':
            return Pc()
        elif device_name == 'laptop':
            return Laptop()
        elif device_name == 'smartphone':
            return Smartphone()
        else:
            raise ValueError('Device does not exist')