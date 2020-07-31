import json

folder = 'part1_basics/chapter10/files/'
filename = 'numbers.json'

with open(f"{folder}{filename}") as f:
    numbers = json.load(f)

print(numbers)