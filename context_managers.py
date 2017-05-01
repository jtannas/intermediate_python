"""
25. Context managers

Context managers allow you to allocate and release resources precisely
when you want to. The most widely used example of context managers is
the with statement. Suppose you have two related operations which you’d
like to execute as a pair, with a block of code in between. Context
managers allow you to do specifically that.
"""

# Example with Open
with open('write_me.txt', 'w') as file:
    file.write('Hola!')

#: The above code opens the file if it exists, creates it if it doesn't
#: and closes it when the with statement finishes.
#: Effectively, it does:
file = open('write_me.txt', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

#: It provides the advantage of making sure the setup and teardown
#: occurs, and it removes the 'administrative logic' from the code.
#: This makes them **superb** for thread-locking in a multi-threaded
#: process.

### IMPLEMENTING AS A CLASS ###################################################
#: At the very least, a context manager has __enter__ and __exit__
#: methods defined.


class MyFile():
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        """Exit method for context managers.

        Args:
            - self: the parent class
            - type: See sys.exc_info()
            - value: See sys.exc_info()
            - traceback: See sys.exc_info()
        """
        self.file_obj.close()


#: This is enough to get started
with MyFile('write_me.txt', 'w') as opened_file:
    opened_file.write('Hola!')

###: Under the Hood
#: 0. The with statement is called.
#: 1. The with statement stores the __exit__ method of File class.
#: 2. It calls the __enter__ method of File class.
#: 3. __enter__ method opens the file and returns it.
#: 4. the opened file handle is passed to opened_file.
#: 5. we write to the file using .write()
#: 6. with statement calls the stored __exit__ method.
#: 7. the __exit__ method closes the file.

### HANDLING EXCEPTIONS #######################################################
"""
We did not talk about the type, value and traceback arguments of the
__exit__ method. Between the 4th and 6th step, if an exception occurs,
Python passes the type, value and traceback of the exception to the
__exit__ method. It allows the __exit__ method to decide how to close
the file and if any further steps are required. In our case we are not
paying any attention to them.

What if our file object raises an exception? We might be trying to
access a method on the file object which it does not supports.
For instance:
"""
with MyFile('write_me.txt', 'w') as opened_file:
    opened_file.nonexistent_function('Hola!')  # Error time


# Let's add some exception handling to the MyFile class
class MyFile_v2(MyFile):
    def __exit__(self, type, value, traceback):
        print("Exception as been handled")
        self.file_obj.close()
        # return True stops 'with' from raising an exception, otherwise
        # it is reraised after __exit__ completes.
        return True


### IMPLEMENTING A CONTEXT MANAGER AS A GENERATOR #############################
from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


with open_file('write_me.txt') as file:
    file.write('Hola!')
"""
Let’s dissect this method a little.

1. Python encounters the yield keyword. Due to this it creates a
    generator instead of a normal function.
2. Due to the decoration, contextmanager is called with the function
    name (open_file) as its argument.
3. The contextmanager function returns the generator wrapped by the
    GeneratorContextManager object.
4. The GeneratorContextManager is assigned to the open_file function.
    Therefore, when we later call open_file function, we are actually
    calling the GeneratorContextManager object.
"""

#: Further Reading
#: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
#: http://preshing.com/20110920/the-python-with-statement-by-example/
