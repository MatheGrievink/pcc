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
| for element in list: <br />&nbsp; print(element) | Print every element in a list | for element in list: <br />&nbsp; print(element) |
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
| if *conditional test*: <br />&nbsp; *do something* | If a conditional value returns true, do code. If you want 1 block of code to run, use elif. Otherwise, use an if.| if 1 = 1 : <br />&nbsp; print("hello")
| if *conditional test*: <br />&nbsp; *do something* <br> else: <br />&nbsp; *other code* | If a conditional value returns true, do code. Else, do other code | if 1 = 1 : <br />&nbsp; print("hello") <br> else: <br />&nbsp; *print("bye")* |
| if *conditional test*: <br />&nbsp; *do something* <br> elif *conditional test*: <br />&nbsp; *do something* <br> else: <br />&nbsp; *other code* | If a conditional value returns true, do code. Elif other match: do code. Else, do other code. You can have multiple elif. | if variable = 1 : <br />&nbsp; print("good morning") <br> elif variable = 2: <br />&nbsp; print("good afternoon") <br> else: <br />&nbsp; print("good evening")|
| list = [] <br /><br /> if list: <br />&nbsp; *if list has items* <br> else: <br />&nbsp; *if list has no items* | Check if a list has items. | requested_toppings = [] <br /><br /> if requested_toppings: <br />&nbsp; *add toppings* <br> else: <br />&nbsp; *there are no toppings selected* |


## Chapter 6 - Dictonaries
| Function | Explanation | Example |
|---|---|---|
| dictionary = {'key1': 'value1', 'key2': 'value2'} | Assign mutiple keys and values to a dictionary | alien = {'color': 'green', 'points': 5} |
