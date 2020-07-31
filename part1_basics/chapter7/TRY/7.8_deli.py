sandwich_orders = ['Salmon', 'Beef', 'Cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Current sandwich: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"The order with an {sandwich} sandwich is done.")