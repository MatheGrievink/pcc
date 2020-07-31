print("Enter two numbers and I'll add them together.")
print("Enter 'q to exit.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You must enter numbers!")
else:
    print(answer)