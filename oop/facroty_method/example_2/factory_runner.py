from pc import *
from laptop import *
from smartphone import *


def create_device(device_name):
    if device_name == 'Smartphone':
        return Smartphone()
    elif device_name == 'Pc':
        return Pc()
    elif device_name == 'Laptop':
        return Laptop()
    else:
        raise ValueError('Device not found')



device = create_device('sdaf')
print(device.specs())