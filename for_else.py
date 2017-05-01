"""
19. For - Else
Loops are an integral part of any language. Likewise for loops are an
important part of Python. However there are a few things which most
beginners do not know about them. We will discuss a few of them one by
one.
"""

### Basic loop example
fruits = ['apple', 'banana', 'mange']
for fruit in fruits:
    print(fruit.capitalize())

### Range loop example
for i in range(len(fruits)):
    print(fruits[i].capitalize)

### In the background...
#: Every for loop has an IF statment hidden inside it to check if the
#: loop should continue running.
if more_items_to_loop_over is True:
    do_stuff()
    repeat_loop()

#: Python's for-else loops let you toss an else statement on to the
#: implied if statement
if more_items_to_loop_over is True:
    do_stuff()
    repeat_loop()
else:
    do_something_else()

#: The else condition is useful for when there is a break statement
#: that terminates the loop before it goes through all the items.


### EXAMPLE TIME ######################################################
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything
    not_found_in_container()

def prime_finder():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f'{n} equals {x}*{n/x}')
                break
        else:
            # loop fell through without finding a factor
            print(f'{n} is a prime number')
