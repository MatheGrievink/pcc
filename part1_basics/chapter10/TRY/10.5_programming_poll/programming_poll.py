filename = 'chapter10/TRY/10.4_guest_book/guest_book.txt'

with open(filename, 'a') as file_object:

    while True:
        user_input = input("What is your name?")

        print(f"Your name has been added to the guest book!\n")
        file_object.write(f"{user_input}\n")