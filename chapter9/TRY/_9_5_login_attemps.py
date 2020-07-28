class User:
    """Create a user."""

    def __init__(self, first, last, age, location):
        """Create attributes"""
        self.first = first
        self.last = last
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe the user."""
        message = f"\nThe user is {self.first.title()} {self.last.title()}."
        message += f"\nHe or she is {self.age} years old and lives in {self.location.title()}."
        print(message)

    def greet_user(self):
        """Greet user"""
        print(f"Hello, {self.first.title()} {self.last.title()}!")

    def show_login_attempts(self):
        """Show the login attempts of an user"""
        print(f"{self.first.title()} {self.last.title()} has {self.login_attempts} login attempts.")

    def increment_login_attemps(self):
        """How many times did an user attempt to login?"""
        self.login_attempts += 1
    
    def reset_login_attemps(self):
        """Reset the login attemps of an user"""
        self.login_attempts = 0

person = User("Mathe", "Grievink", 20, "dinxperlo")
person.describe_user()
person.greet_user()

person.show_login_attempts()
person.increment_login_attemps()
person.increment_login_attemps()
person.increment_login_attemps()
person.increment_login_attemps()
person.show_login_attempts()
person.reset_login_attemps()
person.show_login_attempts()