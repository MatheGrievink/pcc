birth_date = {
    'mathe': [16, 8, 99],
    'joelle': [8, 3, 97],
    'ramon': [4, 6, 95],
    'astrid': [22, 2, 70],
    'erik': [12, 9, 70],
}

for name, numbers in birth_date.items():
    print(f"De geboortedatum van {name.title()} is:")
    for number in numbers:
        print(f"{number}")