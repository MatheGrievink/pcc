def build_car(manufacture, model, **car_info):
    """Build a car with the given options"""
    car_info['manufacture'] = manufacture
    car_info['model'] = model

    return car_info

car = build_car('Mazda', '2', color='white', doors='3')

print(car)