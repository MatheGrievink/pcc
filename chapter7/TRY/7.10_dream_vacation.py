vacations = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    place = input("Where is your dream vacation? ")

    vacations[name] = place

    repeat = input("Would you like to let another person respond? (y/n)")
    if repeat == 'n':
        active = False

print("\n--- Poll Results---")
for name, place in vacations.items():
    print(f"{name} would like to go to {place}.")