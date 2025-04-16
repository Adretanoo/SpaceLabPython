from builder_tour import TourPackageBuilder

tour_builder = TourPackageBuilder()
tour = (tour_builder
        .set_tour_name("Італія Україна")
        .set_destination("Італія")
        .set_hotel("Рошен")
        .set_duration(12)
        .set_transport("Машина")
        .build())

print(tour)


