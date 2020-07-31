sandwich_orders = ['Salmon', 'Beef', 'Cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("There is no pastrami today!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Current sandwich: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"The order with an {sandwich} sandwich is done.")