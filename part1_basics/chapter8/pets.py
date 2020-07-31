def descripe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional Argument
descripe_pet('dog', 'whillie')

# Keyword Argument
descripe_pet(animal_type='hamster', pet_name='harry')

# Default values
def descripe_pet(pet_name,animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

descripe_pet(pet_name='Demi')
descripe_pet('Nola')

#Other value than default
descripe_pet(animal_type='hamster', pet_name='harry')