from tour_package import TourPackage


class TourPackageBuilder:
    def __init__(self):
        self.tour = TourPackage()

    def set_tour_name(self, tour_name):
        self.tour.tour_name = tour_name
        return self

    def set_destination(self, destination):
        self.tour.destination = destination
        return self

    def set_duration(self, duration):
        self.tour.duration = duration
        return self

    def set_hotel(self, hotel):
        self.tour.hotel = hotel
        return self

    def set_transport(self, transport):
        self.tour.transport = transport
        return self


    def build(self):
        return self.tour
