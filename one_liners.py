"""
18. One-Liners
In this chapter I will show you some one-liner Python commands which
an be really helpful.
"""

### SIMPLE WEB SERVER #################################################
# Python 2
#   $ python -m SimpleHTTPServer

# Python 3
#   $ python -m http.server

### PRETTY PRINTING ###################################################
# dictionary
from pprint import pprint
my_dict = {
    'name': 'Yasoob',
    'age': 'undefined',
    'personality': 'awesome',
}
pprint(my_dict)

# json
#   $ cat file.json | python -m json.tool

### PROFILING A SCRIPT ################################################
#   $ python -m cProfile my_script.py

### CSV TO JSON #######################################################
import csv
import json
print json.dumps(list(csv.reader(open('csv_file.csv'))))

### LIST FLATTENING ###################################################
a_list = [
    [1, 2],
    [3, 4],
    [5, 6],
]
a_flat = list(itertools.chain.from_iterable(a_list))
# or
a_flat = list(itertools.chain(*a_list))
print(a_flat)  # Output: [1, 2, 3, 4, 5, 6]


### ONE-LINE CONSTRUCTORS
class A():
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals.items if k != 'self'})
