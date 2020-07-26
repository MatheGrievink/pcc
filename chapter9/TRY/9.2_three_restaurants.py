class Restaurant:
    """A class for a restaurant."""

    def __init__(self, name, cuisine):
        """Create the name of the restaurant and cuisine."""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Desribe the restaurant."""
        print(f"\nThe name of the restaurant is {self.name.title()}.")
        print(f"The cuisine of the restaurant is {self.cuisine}.")

    def open(self):
        """Announce that the restaurant is open!"""
        print("The restaurant is now open!")

restaurant = Restaurant("Gringo's", 'Mexican')
restaurant.describe()

restaurant = Restaurant("Huang", 'Wok')
restaurant.describe()

restaurant = Restaurant("Happy Italy", 'Italian')
restaurant.describe()