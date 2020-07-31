import json

numbers = [2, 3, 5, 7, 11, 13]

folder = 'part1_basics/chapter10/files/'
filename = 'numbers.json'

with open(f"{folder}{filename}", 'w') as f:
    json.dump(numbers, f)