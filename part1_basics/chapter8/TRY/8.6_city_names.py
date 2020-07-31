def city_names(name,country):
    """Show city names"""
    city_name = f"{name.title()}, {country.title()}"
    
    print(city_name)

city_names('amsterdam', 'netherlands')
city_names('berlin', 'germany')
city_names('paris', 'france')