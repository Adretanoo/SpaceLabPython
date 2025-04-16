from car_facotry import CarFactory
from parked_car import ParkedCar

factory = CarFactory()

# Створюємо кілька припаркованих авто
parking_lot = [
    ParkedCar("AA1234XX", 0, 0, factory.get_car("BMW", "X5", "Black")),
    ParkedCar("BB5678YY", 0, 1, factory.get_car("BMW", "X5", "Black")),
    ParkedCar("CC9999ZZ", 1, 0, factory.get_car("Tesla", "Model S", "White")),
    ParkedCar("DD0000WW", 1, 1, factory.get_car("BMW", "X5", "Black")),
]

# Виводимо інформацію
for parked_car in parking_lot:
    parked_car.display()