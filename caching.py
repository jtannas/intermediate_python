"""
24. Function caching
Function caching allows us to cache the return values of a function
depending on the arguments. It can save time when an I/O bound function
is periodically called with the same arguments. Before Python 3.2 we
had to write a custom implementation. In Python 3.2+ there is an
lru_cache decorator which allows us to quickly cache and uncache the
return values of a function.

Let’s see how we can use it in Python 3.2+ and the versions before it.
"""

### PYTHON 3.2+ ###############################################################
from functools import lru_cache


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


[n for n in range(16)]

#: The maxsize argument tells lru_cache about how many recent return
#: values to cache.

# It can be inspected via:
fib.cache_info()

# It can be cleared via:
fib.cache_clear()

### PYTHON 2+ #################################################################
from functools import wraps


def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
