def make_sandwich(*toppings):
    """Make a sandwich"""
    print("\nWe're making a sandwich with:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('salmon')
make_sandwich('bacon', 'cheese')
make_sandwich('lettuce', 'salami', 'bbq sauce')