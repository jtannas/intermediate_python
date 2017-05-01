"""
23. Coroutines
Coroutines are similar to generators with a few differences. The main
differences are:
    - generators are data producers
    - coroutines are data consumers
"""


# Generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Use in a for loop
x = fib()
for i in range(10):
    print(next(x))


#: Coroutines consume values which are sent to it, as they are sent to it.
# Consumer
def grep(pattern):
    print(f"Searching for {pattern}...")
    while True:
        line = (yield)
        if pattern in line:
            print(line)


#: In the grep example, (yield) does not initially contain anyting.
#: We instead supply it with a value using the .send() method.

search = grep('coroutine')
next(search)  # needed to start the coroutine, advancing it to the (yield)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Output: I love coroutines instead!
search.close()
