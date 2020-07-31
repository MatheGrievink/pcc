people = input("How many people are comming for dinner?")
people = int(people)

if people > 8:
    print(f"\nYou have to wait for a table.")
else:
    print(f"\nThe table is ready!")