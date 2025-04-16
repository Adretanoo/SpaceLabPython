from car_flyweight import Car

class ParkedCar:
    def __init__(self, number_plate, row, column, car: Car):
        self.number_plate = number_plate
        self.row = row
        self.column = column
        self.car = car

    def display(self):
        self.car.display(self.number_plate, self.row, self.column)