prompt = input("How old are you?")
prompt = int(prompt)

while True:
    if prompt < 3:
        print("The price is $0")
        break
    elif prompt < 12:
        print("The price is $10")
        break
    else:
        print("The price is $15")
        break