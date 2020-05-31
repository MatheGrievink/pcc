#Create list
squares = []

#for loop to add squares of each number between 1 to 10
for value in range(1,11):
    square = value ** 2
    squares.append(square)

#print the squares
print(squares)


#The same code as above but a bit shorter
#Create list
squares = []

#for loop to add squares of each number between 1 to 10
for value in range(1,11):
    squares.append(value**2)

#print the squares
print(squares)

#The same code as above but a bit shorter
#Create list
squares = [value**2 for value in range(1, 11)]
print(squares)