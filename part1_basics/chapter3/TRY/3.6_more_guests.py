people = ['Steve Jobs', 'Bill Gates', 'Elon Musk']
print(f"Here is your inventation {people[0]}.")
print(f"Here is your inventation {people[1]}.")
print(f"Here is your inventation {people[2]}.")

cant_come = 'Steve Jobs'
people.remove(cant_come)
print(f"{cant_come} can not come to the diner because he is dead.")

people.insert(0, 'Mark Zuckerberg')
print(f"Here is your inventation {people[0]}.")
print(f"Here is your inventation {people[1]}.")
print(f"Here is your inventation {people[2]}.")

print("I've found a bigger dinner table!")
people.insert(2, 'Jeff Bezos')
people.append('Jack')
print(f"Here is your inventation {people[2]}")
print(f"Here is your inventation {people[-1]}")