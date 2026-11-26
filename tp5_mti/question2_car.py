class Car:

    def __init__(self):
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def show(self):
        print("Car configuration:")

        if len(self.options) == 0:
            print("Basic car - No options")
        else:
            for option in self.options:
                print("-", option)


class CarBuilder:

    def __init__(self):
        self.car = Car()

    def add_wheels(self):
        self.car.add_option("Sport wheels")

    def add_roof(self):
        self.car.add_option("Sunroof")

    def add_gps(self):
        self.car.add_option("GPS")

    def add_leather_seats(self):
        self.car.add_option("Leather seats")

    def add_spoiler(self):
        self.car.add_option("Spoiler")


class CarDirector:

    def basic_car(self, builder):
        pass

    def sport_car(self, builder):
        builder.add_wheels()
        builder.add_spoiler()

    def luxury_car(self, builder):
        builder.add_roof()
        builder.add_gps()
        builder.add_leather_seats()


if __name__ == "__main__":

    director = CarDirector()

    builder1 = CarBuilder()
    car1 = builder1.car
    car1.show()

    print("----------------")

    builder2 = CarBuilder()
    director.sport_car(builder2)
    car2 = builder2.car
    car2.show()

    print("----------------")

    builder3 = CarBuilder()
    director.luxury_car(builder3)
    car3 = builder3.car
    car3.show()