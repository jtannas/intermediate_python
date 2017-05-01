"""Python Generators Example"""


def yield_nums(num):
    """Example of how a function can yield a result.

    Yield is similar to return, except that it doesn't fully exit the
    function. This allows results to be returned incrementally, saving
    CPU & memory resource.
    """
    for i in range(num):
        yield i


for item in yield_nums(10):
    print(item)


def fibonacci(num):
    """Fibonacci sequence using generators"""
    a = 1
    b = 1
    for item in range(num):
        yield a
        a, b = b, a + b

for i in fibonacci(3):
    print(f"fib {i}")

my_string = "my_string"
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
