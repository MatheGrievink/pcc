#add cars to the list, sort alphabetic and print
cars = ['bmw', 'audi', 'toyota', 'subaru']

#Original
print("Here is the original list:")
print(cars)

#Sorted list
print("Here is a sorted list:")
print(sorted(cars))

#Original
print("Here is the original list:")
print(cars)
cars.sort()
print(cars)

print("Let's reverse:")
cars.reverse()
print(cars)

#Sort in reverse alphabetic and print
cars.sort(reverse=True)
print(cars)

print(len(cars))

