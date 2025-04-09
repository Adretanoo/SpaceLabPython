class TourPackage:
    def __init__(self):
        self.tour_name = None
        self.destination = None
        self.duration = None
        self.hotel = None
        self.transport = None

    def __str__(self):
        return f"Тур: {self.tour_name}, Місце призначення: {self.destination}, Тривалість: {self.duration} днів, Готель: {self.hotel}, Транспорт: {self.transport}"