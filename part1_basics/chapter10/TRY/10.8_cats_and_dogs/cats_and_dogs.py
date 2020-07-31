def list_names(filename):
    """List the names in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            names = f.readlines()
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} can not be found!")
    else:
        print(f"\nThe file {filename} has the names:")
        for name in names:
            print(f"- {name.strip().title()}")
    
folder = 'chapter10/TRY/10.8_cats_and_dogs/'
filenames = ['cats.txt', 'dogs.txt', 'rabbits.txt']
for filename in filenames:
    list_names(f"{folder}{filename}")