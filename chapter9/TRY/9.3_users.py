class User:
    """Create a user."""

    def __init__(self, first, last, age, location):
        """Create attributes"""
        self.first = first
        self.last = last
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Describe the user."""
        message = f"\nThe user is {self.first.title()} {self.last.title()}."
        message += f"\nHe or she is {self.age} years old and lives in {self.location.title()}."
        print(message)

    def greet_user(self):
        """Greet user"""
        print(f"Hello, {self.first.title()} {self.last.title()}!")

person1 = User("Mathe", "Grievink", 20, "dinxperlo")
person1.describe_user()
person1.greet_user()

person2 = User("Willem", "van oranje", 53, "wassenaar")
person2.describe_user()
person2.greet_user()
