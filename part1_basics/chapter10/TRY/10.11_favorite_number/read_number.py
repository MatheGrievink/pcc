import json

folder = 'part1_basics/chapter10/TRY/10.11_favorite_number/'
filename = 'number.json'

with open(f"{folder}{filename}") as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")