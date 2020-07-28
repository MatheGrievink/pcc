class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """Set the odometer reading to the given value, reject if attemps to roll back."""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        """Add given amount to odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Fill the gass tank"""
        print("Filling the gas tank.")

class Battery:
    """Model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Create the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range of this battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrade the battery."""
        if self.battery_size < 100:
            print("Upgrading the battery!")
            self.battery_size = 100
        else:
            print("You already have the largest battery")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    # Override a method of parent class
    def fill_gas_tank(self):
        """Electric vehicles don't have gas tanks."""
        print("Electric vehicles doesn't need gas!")



my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()