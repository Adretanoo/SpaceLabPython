class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display(self, number_plate, row, column):
        print(f"Car [{self.brand} {self.model}, {self.color}] "
              f"з номером '{number_plate}' парковка в ({row}, {column})")
