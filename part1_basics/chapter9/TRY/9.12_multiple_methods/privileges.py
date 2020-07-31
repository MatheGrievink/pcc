            
class Admin(User):
    """Represents an Admin user"""

    def __init__(self, first, last, age, location):
        """Inhert parent class User"""
        super().__init__(first, last, age, location)
        self.privileges = Privileges()

class Privileges:
    """A class with privileges"""
    
    def __init__(self):
        """List the privileges"""
        self.privileges = ['can delete posts', 'can ban user', 'can add posts']

    def show_privileges(self):
        """Show the privileges of an admin user."""
        print(f"The Admin can: ")
        for privilege in self.privileges:
            print(f"  - {privilege}.")

