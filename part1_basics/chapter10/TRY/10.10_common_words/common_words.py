def count_words(filename, search):
    """Count how many times a specific word appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        search = search.lower()
        num_words = words.count(search)

        print(f"The word '{search}' appears {num_words} times in the file {filename}.")


while True:
    print("What word would you like to search?")
    print("Press 'q' to exit")

    search = input("Enter word: ")
    if search == 'q':
        break
    folder = 'chapter10/TRY/10.10_common_words/'
    filenames = ['frankenstein.txt', 'dracula.txt', 'tale_of_two_cities.txt']
    for filename in filenames:
        count_words(f"{folder}{filename}",search)