"""
20. Python C extensions
An interesting feature offered to developers by the CPython
implementation is the ease of interfacing C code to Python.

There are three key methods developers use to call C functions from
their python code - ctypes, SWIG and Python/C API. Each method comes
with it’s own merits and demerits.

Firstly, why would you want to interface C with Python?
A few common reasons are :
- You want speed and you know C is about 50x faster than Python.
- Certain legacy C libraries work just as well as you want them to, so you don’t want to rewrite them in python.
- Certain low level resource access - from memory to file interfaces.
- Just because you want to.
"""

### 20.1 CTypes #######################################################
"""
The Python ctypes module is probably the easiest way to call C
functions from Python. The ctypes module provides C compatible data
types and functions to load DLLs so that calls can be made to C shared
libraries without having to modify them. The fact that the C side
needn’t be touched adds to the simplicity of this method.
"""
rom ctypes import *

# load th shared object file
adder = CDLL('./adder.so')

# Find sum of integers
res_int = adder.add_int(4, 5)
print(f'Sum of 4 and 5 = {str(res_int)}')

# Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print(f'Sum of 4.1 and 5.5 = {str(add_float(a, b))}')

### 20.2 SWIG #########################################################
"""
Simplified Wrapper and Interface Generator, or SWIG for short is
another way to interface C code to Python. In this method, the
developer must develop an extra interface file which is an input to
SWIG (the command line utility).

Python developers generally don’t use this method, because it is in
most cases unnecessarily complex. This is a great method when you have
a C/C++ code base, and you want to interface it to many different
languages.

See the book for the walkthough.
http://book.pythontips.com/en/latest/python_c_extension.html#swig
"""

### 20.3 Python/C API #################################################
"""
The C/Python API is probably the most widely used method - not for it’s
simplicity but for the fact that you can manipulate python objects in
your C code.

This method requires your C code to be specifically written for
interfacing with Python code. All Python objects are represented as a
PyObject struct and the Python.h header file provides various functions
to manipulate it. For example if the PyObject is also a PyListType
(basically a list), then we can use the PyList_Size() function on the
struct to get the length of the list. This is equivalent to calling
len(list) in python. Most of the basic functions/opertions that are
there for native Python objects are made available in C via the
Python.h header.

See the book for the walkthough.
http://book.pythontips.com/en/latest/python_c_extension.html#python-c-api
"""
