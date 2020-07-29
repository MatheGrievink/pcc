class Restaurant:
    """A class for a restaurant."""

    def __init__(self, name, cuisine):
        """Create the name of the restaurant and cuisine."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Desribe the restaurant."""
        print(f"\nThe name of the restaurant is {self.name.title()}.")
        print(f"The cuisine of the restaurant is {self.cuisine}.")

    def open(self):
        """Announce that the restaurant is open!"""
        print("The restaurant is now open!")
    
    def read_served(self):
        """Print the number of served"""
        print(f"We have served {self.number_served} people.")

    def set_number_served(self, total_served):
        """How many served?"""
        if total_served >= self.number_served:
            self.number_served = total_served
        else:
            print("This number can't be lower than before!!")
    
    def increment_number_served(self, served):
        """Add served to total_served"""
        self.number_served += served

class IceCreamStand(Restaurant):
    """Model an Ice Cream stand"""

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Cookies', 'Vanilla', 'Choclate']

    def show_flavors(self):
        print(f"\nThe Ice Cream stand has the following flavors: ")
        for flavor in self.flavors:
            print(f"  - {flavor}")

stand = IceCreamStand('Claudio', 'Ice Creams')

stand.show_flavors()