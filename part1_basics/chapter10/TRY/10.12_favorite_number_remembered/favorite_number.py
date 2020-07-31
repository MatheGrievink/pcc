import json

def get_stored_number():
    """Get stored number if available."""

    folder = 'part1_basics/chapter10/TRY/10.12_favorite_number_remembered/'
    filename = 'number.json'

    try:
        with open(f"{folder}{filename}") as f:
            number = json.load(f)
    except FileNotFoundError:
        number = input("What is your favorite number? ")
        folder = 'part1_basics/chapter10/TRY/10.12_favorite_number_remembered/'
        filename = 'number.json'

        with open(f"{folder}{filename}", 'w') as f:
            json.dump(number, f)
    else:
        print(f"I know your favorite number. It's {number}.")

get_stored_number()

        