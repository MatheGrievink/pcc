import random

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

my_ticket = random.sample(characters, 4)

print(my_ticket)

i = 0
while True:

    winning = random.sample(characters, 4)

    if winning != my_ticket:
        i += 1
        continue
    else:
        print(f"You have won, this test has ran {i} times!")
        break
