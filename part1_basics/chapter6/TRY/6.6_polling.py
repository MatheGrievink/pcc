favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'darlene', 'edward', 'elliot']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name  not in people:
        print("Thank you for taking the poll.")
    else:
        print("You should take the poll.")