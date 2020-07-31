import json


def get_stored_username():
    """Get stored username if available."""

    folder = 'part1_basics/chapter10/files/'
    filename = 'username.json'

    try:
        with open(f"{folder}{filename}") as f:
            username = json.load(f)
    except:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    folder = 'part1_basics/chapter10/files/'
    filename = 'username.json'

    with open(f"{folder}{filename}", 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        

greet_user()