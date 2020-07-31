class Employee:
    """A class that represents an Employee"""

    def __init__(self, first, last, salery):
        """Store things"""
        self.first = first.title()
        self.last = last.title()
        self.salery = salery

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salery += amount