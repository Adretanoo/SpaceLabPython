class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.engine = None
        self.gps = False
        self.autopilot = False

    def __str__(self):
        return f"{self.brand} {self.model} ({self.color}) - Engine: {self.engine}, GPS: {self.gps}, Autopilot: {self.autopilot}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def add_gps(self):
        self.car.gps = True
        return self

    def add_autopilot(self):
        self.car.autopilot = True
        return self

    def build(self):
        return self.car

# Використання
builder = CarBuilder()
car1 = builder.set_brand("Tesla").set_model("Model S").set_color("Red").set_engine("Electric").add_gps().add_autopilot().build()

print(car1)
