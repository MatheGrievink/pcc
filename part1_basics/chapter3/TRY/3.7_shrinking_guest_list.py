#Add people to the list
people = ['Steve Jobs', 'Bill Gates', 'Elon Musk']

#Invite people
print(f"Here is your inventation {people[0]}.")
print(f"Here is your inventation {people[1]}.")
print(f"Here is your inventation {people[2]}.")

#Remove Steve Jobs from list
cant_come = 'Steve Jobs'
people.remove(cant_come)
print(f"{cant_come} can not come to the diner because he is dead.")

#Add Mark Zuckerberg to the list and invite
people.insert(0, 'Mark Zuckerberg')
print(f"Here is your inventation {people[0]}.")
print(f"Here is your inventation {people[1]}.")
print(f"Here is your inventation {people[2]}.")

#Add more people to the list and invite them
print("I've found a bigger dinner table!")
people.insert(2, 'Jeff Bezos')
people.append('Jack')
print(f"Here is your inventation {people[2]}")
print(f"Here is your inventation {people[-1]}")

#Remove 3 people from the list
print("The new dinner table won't arrive in time for the dinner, I can only invite 2 guests.")
people.pop(-1)
people.pop(-2)
people.pop(-3)

#Invite the last 2 people
print(f"You are still invited to dinner {people[0]}")
print(f"You are still invited to dinner {people[1]}")

#Remove the last 2 people from the list
del people[1]
del people[0]

print(people)