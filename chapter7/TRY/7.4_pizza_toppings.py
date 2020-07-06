prompt = "\nWhat pizza toppings would you like?"
prompt += "\nEnter 'quit' to end the program."

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping} is added to the list!")