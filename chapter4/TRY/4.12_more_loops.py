#Make a list
my_foods = ['pizza', 'falafel', 'carrot cake']

#Copy the list in to other variable
friend_foods = my_foods[:]

#Append into lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)