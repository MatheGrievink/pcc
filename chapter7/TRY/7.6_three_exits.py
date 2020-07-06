prompt = input("How old are you?")
prompt = int(prompt)

active = True
while active:
    if prompt < 3:
        print("The price is $0")
        active = False
    elif prompt < 12:
        print("The price is $10")
        active = False
    else:
        print("The price is $15")
        active = False