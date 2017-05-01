"""4. Map, Filter and Reduce

These are three functions which facilitate a functional approach to
programming. We will discuss them one by one and understand their use
cases.
"""

### MAP ###############################################################
# Map applies a function to all the items in an input_list.
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


# Map can even be applied to lists of functions
def double(x):
    """Doubles the input"""
    return x * 2


def square(x):
    """Squares the input"""
    return x**2


funcs = [double, square]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

### FILTER ############################################################
# Filter returns a list of items for which a function returns true
number_list = range(-5, 5)
negatives = list(filter(lambda x: x < 0, number_list))
print(f"Negatives: {negatives}")

evens = list(filter(lambda x: x % 2 == 0, number_list))
print(f"Evens: {evens}")

### REDUCE ############################################################
# Reduce is a good tool for computing the result of some function
# against all items in a list.
from functools import reduce
reduce_list = [1, 2, 3, 4, 5]

sum_reduce = reduce((lambda x, y: x + y), reduce_list)
print(f"List Sum: {sum_reduce}")

product_reduce = reduce((lambda x, y: x * y), reduce_list)
print(f"List product: {product_reduce}")
