# Python Crash Cource V2

This repository was created for learning Python with the book Python Crash Cource V2.

# Cheatsheet
This is my documentation for the stuff I learned in the chapters.

## Chapter 1 - Getting started
| Function | Explanation | Example |
|---|---|---|
| print() | Show output on screen | print("Hello World!")


## Chapter 2 - Variables and simple data types
| Function | Explanation | Example |
|---|---|---|
| variable = "" | Assign "hello" to the variable message. | message = " hello" |
| variable.title() | Print first letter of every word with a Captial. | " Hello " |
| variable.upper() | Print all words in UPPERCASE. | " HELLO " |
| variable.lower() | Print all words in lowercase. | " hello " |
| print(f"") | Format-String: print the literal output (with variables). | print(f"{message}, Mathé!") |
| variable.rstrip() | Delete whitespace after string. | " hello" |
| variable.lstrip() | Delete whitespace before string. | "hello "|
| variable.strip() | Delete whitespace from string. | "hello" |
| + - * / ** | Add, subtract, multiply, devide and exponent. | 2 + 2, 2 - 2, 2 * 2, 2 / 2, 2 ** 2|
| 2 2.0 | Integer and floats. | Devide is always float |
| x,y,z = 0,0,0 | Assign multiple variables in 1 line. | first,second,third = 1,2,3 |
| CONSTANT = 1 | Constant,  a variable but should not be changed in a program. | MAX_USERS = 2 |
| #Comment | Add a comment which is ignored by Python. | #This is a commment |

## Chapter 3 - Introducing Lists
| Function | Explanation | Example |
|---|---|---|
| list = ['', ''] | A list of things. Things can be added, modified or deleted. | mountainbikes = ['cannondale', 'trek'] |
| print(list[0]) | Access an element in a list, count starts from 0. | print([0]) (output: cannondale) |
| list[0] = '' | Modify an element in a list | mountainbikes[1] = 'rockrider' |
| list.append('') | Add an element to the end of a list | mountainbikes.append('rockrider') |
| list.insert(0, '') | Insert an element to a position in list. Doesn't change existing elements | mountainbikes.insert(0, 'rockrider') |
| del list[0] | Delete element from list. Element can no longer be used. | del mountainbike[1] |
| popped_list = list.pop(0) | Pop (remove) an element from list (and assign to variable). If no position is defined, the last value is popped | popped_mountainbike = mountainbikes.pop(1) |
| list.remove('') | Same as pop, but now with a specific value | mountainbikes.remove('trek') |
| list.sort() | Sort a list permantly alphabetically. | mountainbikes.sort() |
| list.sort(reverse=True) | Sort a list permantly reverse alphabetically. | mountainbikes.sort(reverse=True) |
| sorted(list) | Sort a list temporarily alphabetically. | sorted(mountainbikes)|
| sorted(list, reverse=True)) | Sort a list temporarily reverse alphabetically. | sorted(mountainbikes, reverse=True))  |
| list.reverse() | Reverse a list. To get the original, just do another reverse. | mountainbikes.reverse() |
| len(list) | Print the number of elements in a list. | len(mountainbikes) |
| list[-1] | Get the last element in a list. -2 gets the second to last element | mountainbikes[-1]

## Chapter 4 - Working with lists
| Function | Explanation | Example |
|---|---|---|
| for element in list: <br />&nbsp;&nbsp; print(element) | Print every element in a list | for element in list: <br />&nbsp;&nbsp; print(element) |
| print(1,5,1) | Make a quick list of numbers. This starts with 1 and ends after 4, with step of 1 | print(1,11,2) #Even numbers 2,3,6,8,10 |
| list = list(range(1,6)) | Quickly create a list with the numbers 1,2,3,4,5 | numbers = numbers(range(1,6)) |
| min(list) | Get the minimium value in a list | min(digits) |
| max(list) | Get the maximum value in a list | max(digits) |
| sum(list) | Get the sum value in a list | sum(digits) |
| list = [value**2 for value in range (1,11)] | Create a list for all squares for the numbers 1 until 10 | squares = [value**2 for value in range (1,11)] |
| list[1:2] | Get the 2nd and 3rd element in a list (index starts at 0) | players[1:2] |
| list[:3] | Get the elements until 4th in a list (index starts at 0) | players[:3] |
| list[3:] | Get the elements after the 4th in a list (index starts at 0) | players[3:] |
| list[-3:] | Get the last elements 3 in a list (index starts at 0) | players[-3:] |
| new_list = list[:] | Copy a list | friends_food = my_food[:] |
| tuple = (1, 2) | Create a tulpe. A tuple can't be directly changed. | dimensions = (200, 50) |
| tuple = (2, 1) | Assign new values to the tuple, you have to devine the entire tuple. | dimensions(400, 100) |

## Chapter 5 - If statements
| Function | Explanation | Example |
|---|---|---|
| == != < <= > >= | Equal, not equal, less, less or equal, greater than, greater or equal | 'audi' == 'audi', 'bmw' != 'audi', 19 < 21, 19 <= 21, 21 > 19, 21 >= 19 |
| And, or | Checking multiple conditions. With and both comparisions must match for true, for OR just 1 comparison | 20 > 21 and 20 < 22,  22 > 21 or 20 < 22 |
| In, not in | Check if a value is in a list or not | 'cannondale' in mountainbikes, 'gazelle' not in mountainbikes |
| if *conditional test*: <br />&nbsp;&nbsp; *do something* | If a conditional value returns true, do code. If you want 1 block of code to run, use elif. Otherwise, use an if.| if 1 = 1 : <br />&nbsp;&nbsp; print("hello")
| if *conditional test*: <br />&nbsp;&nbsp;*do something* <br> else: <br />&nbsp;&nbsp; *other code* | If a conditional value returns true, do code. Else, do other code | if 1 = 1 : <br />&nbsp;&nbsp; print("hello") <br> else: <br />&nbsp;&nbsp; *print("bye")* |
| if *conditional test*: <br />&nbsp;&nbsp; *do something* <br> elif *conditional test*: <br />&nbsp;&nbsp; *do something* <br> else: <br />&nbsp;&nbsp; *other code* | If a conditional value returns true, do code. Elif other match: do code. Else, do other code. You can have multiple elif. | if variable = 1 : <br />&nbsp;&nbsp; print("good morning") <br> elif variable = 2: <br />&nbsp;&nbsp; print("good afternoon") <br> else: <br />&nbsp; print("good evening")|
| list = [] <br /><br /> if list: <br />&nbsp;&nbsp; *if list has items* <br> else: <br />&nbsp;&nbsp; *if list has no items* | Check if a list has items. | requested_toppings = [] <br /><br /> if requested_toppings: <br />&nbsp;&nbsp; *add toppings* <br> else: <br />&nbsp;&nbsp; *there are no toppings selected* |


## Chapter 6 - Dictonaries
| Function | Explanation | Example |
|---|---|---|
| dictionary = {'key1': 'value1', 'key2': 'value2'} | Assign mutiple key-value pairs to a dictionary | alien = {'color': 'green', 'points': 5} |
| print(dictionary['key1']) | Print the value of a key | print(alien['color'] )
| dictionary['key3'] = 'value3' | Add a key and value to a dictionary | alien['speed'] = 5 |
| dictionary['key3] = 'value4' | Modify a value of a specific key | alien['color'] = 'yellow' |
| del dictionary['key3'] | Permantently delete a key-value pair | del alien['speed'] |
| print(dictionary.get('key5', 'No value assigned')) | Print the value of a key. If it does not exist, display 'No value assigned'. | print(alien.get('height', 'Height is not set'))
| for key, value in dictionary.items():<br />&nbsp;&nbsp;print(f"\nKey: {key}")<br />&nbsp;&nbsp;print(f"\nValue: {value}") | Loop through all key-value pairs of a dictionary. | for key, value in alien.items():<br />&nbsp;&nbsp;print(f"\nKey: {key}")<br />&nbsp;&nbsp;print(f"\nValue: {value}") |
| for key in dictionary.keys():<br />&nbsp;&nbsp;print(key) | Loop through all keys in a dictionary | for key in alien.keys():<br />&nbsp;&nbsp;print(key) |
| for value in dictionary.values():<br />&nbsp;&nbsp;print(value) | Loop through all values in a dictionary | for value in alien.values():<br />&nbsp;&nbsp;print(value) |
| for key in sorted(dictionery.keys()):<br />&nbsp;&nbsp;print(key) | Loop thourgh all keys in a dictionary in alphabetical order.  | for key in sorted(alien.keys()):<br />&nbsp;&nbsp;print(key) |
| for value in set(dictionary.values()):<br />&nbsp;&nbsp;print(value) | Loop through all values in a dictionary and check for duplicates | for value in set(alien.values())<br />&nbsp;&nbsp;print(value) |
| dictionary_1 = {'key1': 'value1', 'key2': 'value2'}<br /><br />dictionary_2 = {'key1': 'value1', 'key2': 'value2'}<br /><br />dictionaries = [dictionary_1, dictionary_2]<br /><br />for dictionary in dictionaries:<br />&nbsp;&nbsp;print(dictionary) | Create a list of dictionaries | alien_1 = {'color': 'green', 'points': '5'}<br /><br />alien_2 = {'color': 'yellow', 'points': '10'}<br /><br />aliens = [alien_1, alien_2]<br /><br />for alien in aliens:<br />&nbsp;&nbsp;print(alien) |
| dictionary = {'key1': 'value1', 'key2': ['item1', 'item2'],}<br /><br />print(dictionary['item1'])<br /><br />for item in dictionary['key2']:<br />&nbsp;&nbsp;print(f"\t{item})| A list in a dictionary | pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'cheese'],}<br /><br />print(pizza['crust'])<br /><br />for topping in pizza['toppings']:<br />&nbsp;&nbsp;print(f"\t{topping}) |
| dictionary = {<br />&nbsp;&nbsp;'key1': {<br />&nbsp;&nbsp;&nbsp;&nbsp;'sub_key1': 'sub_value1',<br />&nbsp;&nbsp;&nbsp;&nbsp;'sub_key2': 'sub_value2'<br />&nbsp;&nbsp;},<br /><br />'key2': {<br />&nbsp;&nbsp;&nbsp;&nbsp;'sub_key1': 'sub_value1',<br />&nbsp;&nbsp;&nbsp;&nbsp;'sub_key2': 'sub_value2'<br />&nbsp;&nbsp;},<br />}<br /><br /> for key, key_info in dictionary.items():<br />&nbsp;&nbsp;print(f"\nKey: {key})<br /><br />&nbsp;&nbsp;print(f"\tSub_key1:{key_info]['sub_key1]}")<br />&nbsp;&nbsp;print(f"\tSub_key2:{key_info]['sub_key2]}") | Dictionary in a dictionary | afkortingen = {<br />&nbsp;&nbsp;'mg': {<br />&nbsp;&nbsp;&nbsp;&nbsp;'voor': 'mathe',<br />&nbsp;&nbsp;&nbsp;&nbsp;'achter': 'grievink'<br />&nbsp;&nbsp;},<br /><br />'jg': {<br />&nbsp;&nbsp;&nbsp;&nbsp;'voor': 'joelle',<br />&nbsp;&nbsp;&nbsp;&nbsp;'achter': 'grievink'<br />&nbsp;&nbsp;},<br />}<br /><br /> for afkorting, afkorting_info in afkortingen.items():<br />&nbsp;&nbsp;print(f"\nafkorting: {afkorting})<br /><br />&nbsp;&nbsp;print(f"\tVoor:{afkorting_info]['voor]}")<br />&nbsp;&nbsp;print(f"\tAchter:{afkorting_info]['achter]}") |

## Chapter 7 - User input and while loops
| Function | Explanation | Example |
|---|---|---|
| message = input("user input") | Ask a user for input | age = input("What is your age?") |
| message = input("user input")<br />message += "another rule" | Ask a user for input on multiple lines | age = input("What is your age?")<br />message += "We ask this for the test." |
| int(message) | Convert a string to a numer | age = int(age) |
| 4 % 3 | Give remainder after devide | 100 % 10 (results in 0), 99 % 10 (results in 9) |
| input = 1<br />while input <= 5:<br />&nbsp;&nbsp;print(input)<br />&nbsp;&nbsp;input+=1 | A simple while loop | input = 1<br />while input <= 5:<br />&nbsp;&nbsp;print(input)<br />&nbsp;&nbsp;input+=1 |
| prompt="Typ something"<br />message = "" <br />while message != 'quit':<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message) | A while loop that quits when quit is entered |prompt="Typ something"<br />message = "" <br />while message != 'quit':<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message) |
| prompt="Typ something"<br />message = "" <br />active = True while active:<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message)<br />&nbsp;&nbsp;active = False | A while loop that quits with a flag when quit is entered | prompt="Typ something"<br />message = "" <br />active = True while active:<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message)<br />&nbsp;&nbsp;active = False |
| prompt="Typ something"<br />message = "" <br />active = True while active:<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message)<br />&nbsp;&nbsp;break | A while loop that quits when quit is entered | prompt="Typ something"<br />message = "" <br />active = True while active:<br />&nbsp;&nbsp;message=input(prompt)<br />&nbsp;&nbsp;print(message)<br />&nbsp;&nbsp;break |
| current_number = 0<br /> while current_number < 10:<br />&nbsp;&nbsp;current_number += 1<br />&nbsp;&nbsp;if current_number % 2 == 0:<br />&nbsp;&nbsp;&nbsp;&nbsp;continue<br /><br />&nbsp;&nbsp;print(current_number) | A while loop that runs rest of code before breaking | current_number = 0<br /> while current_number < 10:<br />&nbsp;&nbsp;current_number += 1<br />&nbsp;&nbsp;if current_number % 2 == 0:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue<br /><br />&nbsp;&nbsp;print(current_number) |
| x = 1 <br />while x < 5:<br />&nbsp;&nbsp;print(x) | An infinite loop | x = 1 <br />while x < 5:<br />&nbsp;&nbsp;print(x) |
| old_list = ['item1', 'item2', 'item3']<br />new_list = []<br /><br />while old_list:<br />&nbsp;&nbsp;current_item = old_list.pop()<br />&nbsp;&nbsp;new_list.append(current_item) | Move items between lists | unconfirmed_users = ['user1', 'user2', 'user3']<br />confirmed_users = []<br /><br />while unconfirmed_users:<br />&nbsp;&nbsp;current_user = unconfirmed_users.pop()<br />&nbsp;&nbsp;confirmed_users.append(current_user) |
| list = ['item1', 'item2', 'item1', 'item3'] <br />while 'item1' in list:<br />&nbsp;&nbsp;list.remove('item1') | Remove occurrences of an item from a list |  pets = ['dog', 'cat', 'dog', 'fish'] <br />while 'dog' in pets:<br />&nbsp;&nbsp;pets.remove('dog') |
| dictionary = {}<br><br>active=True<br><br>while active:<br />&nbsp;&nbsp;key = input("Key")<br />&nbsp;&nbsp;value = input("Value")<br><br />&nbsp;&nbsp;dictionary[key] = value<br><br />&nbsp;&nbsp;repeat = input("Fill in another?")<br />&nbsp;&nbsp;if repeat == 'no':<br />&nbsp;&nbsp;&nbsp;&nbsp;active = False | Fill in a dictionary through user input | responses = {}<br><br>active=True<br><br>while active:<br />&nbsp;&nbsp;Name = input("What is your name?")<br />&nbsp;&nbsp;food = input("What would you like to eat?")<br><br />&nbsp;&nbsp;reponses[name] = food<br><br />&nbsp;&nbsp;repeat = input("Fill in another?")<br />&nbsp;&nbsp;if repeat == 'no':<br />&nbsp;&nbsp;&nbsp;&nbsp;active = False |


## Chapter 8 - Functions
| Function | Explanation | Example |
|---|---|---|
| def function():<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;print("Hello")<br><br>fucntion() | Define a function and use it |  def welcome():<br>&nbsp;&nbsp;"""Greet the user"""<br>&nbsp;&nbsp;print("Hello")<br><br>welcome() |
| def function(variable):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;print(variable)<br><br>fucntion("variable") | Define a function and use it |  def welcome(message):<br>&nbsp;&nbsp;"""Greet the user"""<br>&nbsp;&nbsp;print(message)<br><br>welcome("Hello!") |
| def fucntion(parameter1, parameter2)<br><br>function('value1', 'value2') | A function with multiple parameters. | def descripe_pet(animal_type, pet_name)<br><br>function('dog', 'demi') |
| def fucntion(parameter1, parameter2)<br><br>function(parameter1='value1', parameter2='value2') | A function with multiple parameters, called by keywords. | def descripe_pet(animal_type, pet_name)<br><br>function(animal_type='dog', pet_name='demi') |
| def fucntion(parameter1, parameter2='value2')<br><br>function('value1') | A function with multiple parameters. One default parameter. | def descripe_pet(animal_type, pet_name="Nola")<br><br>descripe_pet('dog') |
| def function(value1, value2):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;complete = f"{value1} {value2}"<br>&nbsp;&nbsp;return complete.title()<br><br>input = function('value1', 'value2')<br>print(input) | Returning values | def formatted_name(first_name, last_name):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;full_name = f"{first_name} {last_name}"<br>&nbsp;&nbsp;return full_name.title()<br><br>name = formatted_name('Mathé', 'Grievink')<br>print(name) |
| def function(value1, value2, value3=''):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;if value3:<br>&nbsp;&nbsp;&nbsp;&nbsp;complete = f"{value1} {value2} {value3}"<br>&nbsp;&nbsp;else:<br>&nbsp;&nbsp;&nbsp;&nbsp;complete = f"{value1} {value2}"<br>&nbsp;&nbsp;return complete.title()<br><br>input = function('value1', 'value2')<br>print(input)<br>input = function('value1', 'value2','value3')<br>print(input)  | Returning values with optional value| def formatted_name(first, last, middle=''):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;if middle:<br>&nbsp;&nbsp;&nbsp;&nbsp;full_name = f"{first} {middle} {last}"<br>&nbsp;&nbsp;else:<br>&nbsp;&nbsp;&nbsp;&nbsp;full_name = f"{first} {last}"<br>&nbsp;&nbsp;return full_name.title()<br><br>name = formatted_name('Joe', 'Biden')<br>print(name)<br>name = formatted_name('Donald', 'Trump', 'J.')<br>print(name)  |
| def function(value1, value2, value3=None):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;variable = {'value1' = value1, 'value2' = value2}<br>&nbsp;&nbsp;if value3:<br>&nbsp;&nbsp;&nbsp;&nbsp;variable['value3] = value3<br>&nbsp;&nbsp;return variable<br><br>input = function('value1','value2')<br>print(input)<br>input = function('value1','value2', value3='value')<br>print(input) | Returning a dictionary | def build_person(first_name, last_name):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;person = {'first' = first_name, 'last' = last_name}<br>&nbsp;&nbsp;if age:<br>&nbsp;&nbsp;&nbsp;&nbsp;person['age] = age<<br>&nbsp;&nbsp;return person<br><br>input = build_person('Mathé','Grievink')<br>print(input)<br>input = build_person('Mathé','Grievink', age=20)<br>print(input) | 
| def function(value1, value2):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;complete = f"{value1} {value2}"<br>&nbsp;&nbsp;return complete.title()<br><br> while True: <br>&nbsp;&nbsp;print("\nPlease tell something:")<br>&nbsp;&nbsp;print("(enter 'q' at any time to quit)")<br><br>&nbsp;&nbsp;val_1 = input("Enter the first value: ")<br>&nbsp;&nbsp;if val_1 == 'q':<br>&nbsp;&nbsp;&nbsp;&nbsp;break<br>&nbsp;&nbsp;val_2 = input("Enter the second value: ")<br>&nbsp;&nbsp;if val_2 == 'q':<br>&nbsp;&nbsp;&nbsp;&nbsp;break<br><br>&nbsp;&nbsp;input = function(val_1, val_2)<br>&nbsp;&nbsp;print(f"\n{input}")| Returning values | def get_formatted_name(first_name, last_name):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;full_name = f"{first_name} {last_name}"<br>&nbsp;&nbsp;return full_name.title()<br><br> while True: <br>&nbsp;&nbsp;print("\nPlease tell your name:")<br>&nbsp;&nbsp;print("(enter 'q' at any time to quit)")<br><br>&nbsp;&nbsp;f_name = input("First name: ")<br>&nbsp;&nbsp;if f_name == 'q':<br>&nbsp;&nbsp;&nbsp;&nbsp;break<br>&nbsp;&nbsp;l_name = input("Last name: ")<br>&nbsp;&nbsp;if l_name == 'q':<br>&nbsp;&nbsp;&nbsp;&nbsp;break<br><br>&nbsp;&nbsp;formatted_name = get_formatted_name(f_name, l_name)<br>&nbsp;&nbsp;print(f"\nHello, {formatted_name}")
| def function(values):<br>&nbsp;&nbsp;"""What does the funciton do?"""<br>&nbsp;&nbsp;for value in values:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(value)<br><br>list = ['item1', 'item2']<br>funciton(list) | Passing a list into a function| def greet_users(names):<br>&nbsp;&nbsp;"""Print the names"""<br>&nbsp;&nbsp;for name in names:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(name)<br><br>usernames = ['bob', 'John']<br>greet_users(usernames) |
| def move_items(old_list, new_list):<br>&nbsp;&nbsp;"""What does the function do?"""<br><br>&nbsp;&nbsp;while old_list:<br>&nbsp;&nbsp;&nbsp;&nbsp;current_item = old_list.pop()<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"Current item: {current_item}")<br>&nbsp;&nbsp;&nbsp;&nbsp;new_list.append(current_item)<br><br>def show_items(new_list):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;print("\nThe following items have been moved:")<br>&nbsp;&nbsp;for item in new_list:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(item)<br><br> old_list = ['item1', 'item2']<br>new_list = []<br><br>move_items(old_list,new_list)<br>show_items(new_list) | Move items between 2 lists with functions | def print_models(unprinted, completed):<br>&nbsp;&nbsp;"""Move items between 2 lists"""<br><br>&nbsp;&nbsp;while unprinted:<br>&nbsp;&nbsp;&nbsp;&nbsp;current_item = unprinted.pop()<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"Current item: {current_item}")<br>&nbsp;&nbsp;&nbsp;&nbsp;completed.append(current_item)<br><br>def show_items(completed):<br>&nbsp;&nbsp;"""Show completed items"""<br>&nbsp;&nbsp;print("\nThe following items have been printed:")<br>&nbsp;&nbsp;for item in completed:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(item)<br><br> unprinted = ['item1', 'item2']<br>completed = []<br><br>print_models(unprinted,completed)<br>show_items(completed) |
| *function(lists[:]) | Copy a list into a function | print_models(unprinted[:]) |
| def function(*values)<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;for value in values:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(value)<br><br>function('item')<br>function('item1', 'item2', 'item3') | Passing a arbitrary number of arguments into a function |  def make_pizza(*toppings)<br>&nbsp;&nbsp;"""Make pizza"""<br>&nbsp;&nbsp;print("\nMaking a pizza with:")<br>&nbsp;&nbsp;for topping in topppings:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"- {topping}")<br><br>make_pizza('pepperoni')<br>make_pizza('mushrooms', 'green peppers', 'extra cheese') |
| def function(value, *items)<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;print(value)<br>&nbsp;&nbsp;for item in items:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(item)<br><br>function('item')<br>function('item1', 'item2', 'item3') | Passing a arbitrary number of arguments into a function |  def make_pizza(size, *toppings)<br>&nbsp;&nbsp;"""Make pizza"""<br>&nbsp;&nbsp;print(f"\nMaking a {size}-inch pizza with:")<br>&nbsp;&nbsp;for topping in topppings:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"- {topping}")<br><br>make_pizza(16, 'pepperoni')<br>make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') |
| def function(first, last, **dictionary):<br>&nbsp;&nbsp;"""What does the function do?"""<br>&nbsp;&nbsp;dictionary['first'] = first<br>&nbsp;&nbsp;dictionary['last'] = last<br>&nbsp;&nbsp;return dictionary<br><br>info = function('first', 'last', age=0, location='')<br>print(info) | Fill a dictionary with a function and arbitrary keyword arguments | def build_person(first, last, **user_info):<br>&nbsp;&nbsp;"""Build a profile"""<br>&nbsp;&nbsp;user_info['first_name'] = first<br>&nbsp;&nbsp;user_info['last_name'] = last<br>&nbsp;&nbsp;return user_info<br><br>user = user_info('Mathé', 'Grievink', age=20, location='Dinxperlo')<br>print(user_info) |
| import *module*<br><br>*module*.*function()*| Import a module | import pizza <br><br>pizza.make_pizza() |
| from *module* import *fucntion*<br><br>*function()* | Import a specific function | from pizza import make_pizza<br><br>make_pizza() |
| from *module* import *function* as *alias*<br><br>*alias()* | Import a specific function as an alias | from pizza import make_pizza as mp<br><br>mp() |
| from *module* as *alias*<br><br>*alias*.*function* | Import a module as an alias | from pizza as p<br><br>p.make_pizza() |
| from *module* import function() | Import all functions in a module | from pizza import *<br><br>make_pizza() |

## Chapter 9 - Classes
| Function | Explanation | Example |
|---|---|---|
| class Class:<br>&nbsp;&nbsp;"""What does this class do?"""<br><br>&nbsp;&nbsp;def __init__(self,attribute1,attribute2):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Create attributes"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.attribute1 = attribute1<br>&nbsp;&nbsp;&nbsp;&nbsp;self.attribute2 = attribute2<br><br>&nbsp;&nbsp;def method(self):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""A method"""<br>&nbsp;&nbsp;&nbsp;&nbsp;print(self.attribute1)<br><br>something = Class('attribute1', 'attribute2')<br>something.method() | Create a simple class, create an instance and call a Method. | class Car:<br>&nbsp;&nbsp;"""Create a simple car"""<br><br>&nbsp;&nbsp;def __init__(self,make,model):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Create attributes for the Car"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.make = make<br>&nbsp;&nbsp;&nbsp;&nbsp;self.model = model<br><br>&nbsp;&nbsp;def car_details(self):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""A method to show the car make and model"""<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"This is an {self.make} {self.model}")<br><br>my_car = Car('Mazda', '2')<br>my_car.car_details() |
| self.attribute = 0 | Create a default value for an attribute | self.odometer_reading = 0 |
| something.attribute = 10 | Modify attribute value directly | my_car.odometer_reading = 10 |
| class Class:<br>&nbsp;&nbsp;*--snip init--*<br>&nbsp;&nbsp;def change_attribute(self, value):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Change attribute"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.attribute = value <br><br>*--snip instance--*<br>something.change_attribute(10) | Change a attribute through a method| class Car:<br>&nbsp;&nbsp;*--snip init--*<br>&nbsp;&nbsp;def update_odometer(self, mileage):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Change odometer"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.odometer_reading = mileage <br><br>*--snip instance--*<br>my_car.update_odometer(10) |
| class Class:<br>&nbsp;&nbsp;*--snip init--*<br>&nbsp;&nbsp;def increment_attribute(self, value):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Increment attribute"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.attribute += value <br><br>*--snip instance--*<br>something.increment_attribute(10) | Increment a attribute through a method | class Car:<br>&nbsp;&nbsp;*--snip init--*<br>&nbsp;&nbsp;def increment_odometer(self, miles):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Increment odometer"""<br>&nbsp;&nbsp;&nbsp;&nbsp;self.odometer_reading += miles <br><br>*--snip instance--*<br>my_car.increment_odometer(10) |
| *--snip class Class--*<br><br>class NewClass(Class)<br>&nbsp;&nbsp;"""Create a new class with inheritance"""<br><br>&nbsp;&nbsp;def __init__(self,perant_parameter1, perant_parameter2):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Create attributes from parent class"""<br>&nbsp;&nbsp;super().__init__(perant_parameter1, parent_parameter2)<br><br>something = NewClass('parameter1','parameter2') | Create a new class with inherantance from another class | *--snip class Car--*<br><br>class ElectricCar(Car)<br>&nbsp;&nbsp;"""Create a new class with inheritance"""<br><br>&nbsp;&nbsp;def __init__(self,make, model):<br>&nbsp;&nbsp;&nbsp;&nbsp;"""Create attributes from parent class"""<br>&nbsp;&nbsp;super().__init__(make, model)<br><br>my_other_car = ElectricCar('Tesla','model s') | 
| from file import Class,NewClass | import a class from another file | from car import Car,ElectricCar |
| from random import randint<br>print(randint(1,6)) | Use randint from random module to select a number between 1 and 6 | from random import randint<br>print(randint(1,6)) | 
| from random import choice<br>list = ['value1', 'value2', 'value3']<br>print(choice(list)) | Use choice from random module to select a value from a list | from random import choice<br>list = ['value1', 'value2', 'value3']<br>print(choice(list)) |