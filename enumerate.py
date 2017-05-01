"""
13. Enumerate
Enumerate is a built-in function of Python. It’s usefulness can not be
summarized in a single line. Yet most of the newcomers and even some
advanced programmers are unaware of it. It allows us to loop over
something and have an automatic counter.
"""

some_list = ['a','b','c','d','e']
for counter, value in enumerate(some_list):
    print(f"{counter}: {value}")

# You can also pass it an argument for the starting value of the counter
for counter, value in enumerate(some_list, 3):
    print(f"{counter}: {value}")

# It can also be used to generate tuples from a list
counter_list = list(enumerate(some_list, 1))


#: Side note, it is useful for if you want to change for loops from
#:      for i in range(len(my_list)-1)
#: to
#:      for counter, value in my_list
#: since it gives you both the value and the index in one go.