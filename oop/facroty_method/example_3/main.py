from factory import DeviceFactory

device = DeviceFactory().create_device('Laptop')
print(device.specs())
