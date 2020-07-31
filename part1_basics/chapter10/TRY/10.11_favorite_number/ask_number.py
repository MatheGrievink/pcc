import json

number = input("What is your favorite number? ")
folder = 'part1_basics/chapter10/TRY/10.11_favorite_number/'
filename = 'number.json'

with open(f"{folder}{filename}", 'w') as f:
    json.dump(number, f)