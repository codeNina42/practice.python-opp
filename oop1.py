class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f"Car made in {self.year}, {self.make} {self.model}")

my_car = Car("Toyota", "Corolla", 2021)
my_car.describe()
