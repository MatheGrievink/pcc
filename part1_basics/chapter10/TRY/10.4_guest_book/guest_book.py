filename = 'chapter10/TRY/10.5_programming_poll/programming_poll.txt'

with open(filename, 'a') as file_object:

    while True:
        user_input = input("Why do you like programming?")

        print(f"Your reason has been added!\n")
        file_object.write(f"{user_input}\n")