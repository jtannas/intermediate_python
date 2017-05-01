"""
7. Decorators

Decorators are a significant part of Python. In simple words: they are
functions which modify the functionality of another function. They
help to make our code shorter and more Pythonic. Most of the beginners
do not know where to use them so I am going to share some areas where
decorators can make your code more concise.
"""

# 7.1 Everything in Python is an object
print('\n 7.1')


def hi(name='Joel'):
    return 'hi ' + name


print(hi())

greet = hi

print(greet())

# 7.2 Functions inside functions
print('\n 7.2')


def hi2(name='Joel'):
    print('Running hi2')

    def cheers():
        return 'This is the cheers function'

    def welcome():
        return 'This is the welcome function'

    print(cheers())
    print(welcome())
    print('Ending the hi2 function')


hi2()

# 7.3 Returning Functions
print('\n 7.3')


def hi3(name='Joel'):
    def greet3():
        return 'This is the greet3 function'

    def welcome3():
        return 'This is the welcome3 function'

    if name == 'Joel':
        return greet3
    else:
        return welcome3


var = hi3()
print(var)
print(var())

# 7.4 Giving a function as an argument to another function
print('\n 7.4')


def hi4():
    return 'hi Joel'


def hi4_wrapper(func):
    print('I am printed before hi4')
    print(func())
    print('I am printed after hi4')


hi4_wrapper(hi4)

# 7.5 Writing your first decorator
print('\n 7.5')


# version 1
def decorator5(func):
    def wrap_the_function():
        print('I am getting ready before executing func')
        func()
        print('I am cleaning up after func')

    return wrap_the_function


def decorate_me():
    print('I hope someone setup for me and cleans up after')


decorate_me()

print('Wrapping function... \n')
decorate_me = decorator5(decorate_me)
decorate_me()

print('\n')


# version 2
@decorator5
def decorate_me2():
    print('This is the second function needing decoration')


decorate_me2()

print("\nprinting decorate_me2's name...")
print(decorate_me2.__name__)
print('Uh oh... Time to use functools \n')

# version 3
from functools import wraps


def decorator5_v2(func):
    @wraps(func)
    def my_wrapper():
        print('2nd version of setup')
        func()
        print('2nd version of teardown')

    return my_wrapper


@decorator5_v2
def we_did_it():
    print('We learned to make a decorator!')


we_did_it()


### EXAMPLES ##########################################################
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)


# 7.6.1 Decorators with arguments
def logit2(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')

        return wrapped_function

    return logging_decorator


@logit2(logfile='example.log')
def myfunc1():
    pass


myfunc1()
# Output: myfunc1 was called
# A file called example.log now exists, with the above string


@logit2(logfile='func2.log')
def myfunc2():
    pass


myfunc2()

# Output: myfunc2 was called
# A file called func2.log now exists, with the above string


# 7.6.2 Decorator Classes, with subclassing for added features
class logit3(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self.logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

    def notify(self):
        # logit only logs, no more
        pass


@logit3
def myfunc3():
    pass


class email_logit(logit3):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        pass


@email_logit
def myfunc4():
    pass
