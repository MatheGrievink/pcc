# Just import
import pizza2

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Import specific function
from pizza2 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Import specific function as alias
from pizza2 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# as alias
from pizza2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Import all functions in a module
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


