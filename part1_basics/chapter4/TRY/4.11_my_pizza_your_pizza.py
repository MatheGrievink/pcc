#Make list
my_pizzas = ['BBQ', 'hawaii', 'polo']

#Copy list
friends_pizzas = my_pizzas[:]

#add pizzas
my_pizzas.append('salami')
friends_pizzas.append('shoarma')

#For loop for my pizza
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

#For loop for my pizza
print("My friend's pizzas are:")
for pizza in friends_pizzas:
    print(pizza)