"""
14. Object introspection

In computer programming, introspection is the ability to determine the
type of an object at runtime. It is one of Python’s strengths.
Everything in Python is an object and we can examine those objects.
Python ships with a few built-in functions and modules to help us.
"""

### 14.1 DIR ##########################################################
#: Returns a list of attributes and methods belongin to an object.
mylist = [1, 2, 3]
print(dir(mylist))

### 14.2 TYPE AND ID ##################################################
#: The type function returns the type on an object. For example:
print(type(''))  # Output: <type 'str'>
print(type([]))  # Output: <type 'list'>
print(type({}))  # Output: <type 'dict'>
print(type(dict))  # Output: <type 'dict'>
print(type(3))  # Output: <type 'int'>

#: id returns the unique ids of various objects. For instance:
name = 'Yasoob'
print(id(name))
# Output: 139972439030304

### 14.3 INSPECT MODULE ###############################################
#: The inspect module also provides several useful functions to get
#: information aout live objects. For example you can check the members
#: of an object by running:
import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...
