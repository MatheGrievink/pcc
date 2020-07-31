import json


def get_stored_username():
    """Get stored username if available."""

    folder = 'part1_basics/chapter10/TRY/10.13_verify_user/'
    filename = 'verify_user.json'

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
    folder = 'part1_basics/chapter10/TRY/10.13_verify_user/'
    filename = 'verify_user.json'

    with open(f"{folder}{filename}", 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""

    username = get_stored_username()

    if username:
        user = input("What is your username? ")
        
        if user == username:
            print(f"Welcome back, {username}!")
        else:
            print("It looks like you didn't register before.")
            print("Enter your new username: ")
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        

greet_user()