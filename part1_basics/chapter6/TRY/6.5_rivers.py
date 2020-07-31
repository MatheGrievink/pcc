rivers = {
    'Nile': 'Egypt',
    'Missisipi': 'US',
    'Rhine': 'Germany',
    }

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nThe rivers that where mentioned:")
for river in set(rivers.keys()):
    print(river)

print("\nThe countries that where mentioned:")
for country in set(rivers.values()):
    print(country)