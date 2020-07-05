cities = {
    'dinxperlo': {
        "country": "nederland",
        "population": 7000,
        "fact": "Heeft het kleinste kerkje van Nederland",
    },
    
    'bocholt': {
        "country": "duitsland",
        "population": 72000,
        "fact": "In Bocholt zit een wokrestaurant"
    },

    'parijs': {
        "country": "frankrijk",
        "population": 2148000,
        "fact": "In Parijs staat de Eiffeltoren"
    },
}

for city, city_info in cities.items():
    print(f"\nCtiy: {city.title()}")
    
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}.")