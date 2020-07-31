def city_country(city, country, population=''):
    """Display a city name and a country."""
    
    if population:
        message = f"{city.title()}, {country.title()} - population {population}."
    else:
        message = f"{city.title()}, {country.title()}."
    return message