import json

folder = 'part1_basics/chapter10/files/'
filename = 'username.json'

with open(f"{folder}{filename}") as f:
    username = json.load(f)
    print(f"Welcome back, {username}")