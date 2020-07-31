filename = 'chapter10/TRY/10.3_guest/guest.txt'

with open(filename, 'w') as file_object:
    user_input = input("What is your name? ")

    file_object.write(user_input)