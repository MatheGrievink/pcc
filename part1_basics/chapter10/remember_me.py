import json

username = input("What is your name? ")

folder = 'part1_basics/chapter10/files/'
filename = 'username.json'

with open(f"{folder}{filename}", 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")