#AND
age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print(True)

else:
    print(False)

#AND
age_0 = 22
age_1 = 23
if (age_0 >= 21) and (age_1 >= 21):
    print(True)

else:
    print(False)

#OR
age_0 = 22
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
    print(True)

else:
    print(False)

#IN
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)

if 'pepperoni' in requested_toppings:
    print(True)

else:
    print(False)