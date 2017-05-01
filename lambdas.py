"""
17. Lambdas
Lambdas are one line functions. They are also known as anonymous
functions in some other languages. You might want to use lambdas when
you don’t want to use a function twice in a program. They are just like
normal functions and even behave like them.

A better name for Lambda would've been make_function, but they were
brought into programming decades ago and we're stuck with the name.

They're use for short & simple functions (ie. 1 line - no side effects).
"""

#: Blueprint
#: lambda argument: manipulate(argument)

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

#: Here are some useful use cases for lambdas

# sorting
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

# filtering
a = filter(lambda x: x[0] % 2 == 1, a)
for val in a:
    print(val)
