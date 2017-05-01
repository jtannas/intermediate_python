"""
10. __slots__ Magic
In Python every class can have instance attributes. By default Python
uses a dict to store an object’s instance attributes. This is really
helpful as it allows setting arbitrary new attributes at runtime.

However, for small classes with known attributes it might be a
bottleneck. The dict wastes a lot of RAM. Python can’t just allocate
a static amount of memory at object creation to store all the
attributes. Therefore it sucks a lot of RAM if you create a lot of
objects (I am talking in thousands and millions). Still there is a way
to circumvent this issue. It involves the usage of __slots__ to tell
Python not to use a dict, and only allocate space for a fixed set of
attributes. Here is an example with and without __slots__:

"""


# Without slots
class MyClass1(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass


# With slots
class MyClass2(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass


#: In essence, it is telling Python that the class will take up a fixed
#: amount of space and that it can optimize memory around that fixed
#: amount.
#: Some people have reported RAM savings of 40 to 50% using this.
#: Side note from author: You may want to give PyPy a try. It does all
#: these optimizations by default.
