number = input("What number do you have in mind?")
number = int(number)

remaning = number % 10

if remaning == 0:
    print(f"\nThe number is a multiple of 10!")
else:
    print(f"\nThe number is not a multiple of 10...")