favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Print keys and values:")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite langurage is {language.title()}.")

print("\nPrint keys:")
for name in favorite_languages.keys():
    print(name.title())

print("\nNot in:")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\nPrint with If/else")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\nLoop keys sorted")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nPrint all the values and check for dubble values.")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())