class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback an odometer!")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage

# class ElectricCar that extends Car

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.batery_size = 75

    def describe_battery(self):
        print(f"THis car has {self.battery_size} KWh battery")

