"""
12. Collections

Python ships with a module that contains a number of container data
types called Collections. We will talk about a few of them and discuss
their usefulness.

The ones which we will talk about are:
    - defaultdict
    - OrderedDict
    - counter
    - deque
    - namedtuple
    - enum.Enum (outside of the module; Python 3.4+)
"""
### 12.1 defaultdict ##################################################
from collections import defaultdict
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
) # yapf: disable

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
# Output:
# defaultdict(<class 'list'>,
#   {'Yasoob': ['Yellow', 'Red'],
#   'Ali': ['Blue', 'Black'],
#   'Arham': ['Green'],
#   'Ahmed': ['Silver']
#   })

### Useful use case
# Problem:
# some_dict = {}
# some_dict['colours']['favorite'] = 'yellow'  # Raises KeyError: 'colours'

# Solution:
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favorite'] = 'yellow'  # ^_^

### You can print it using json.dumps
import json
print(json.dumps(some_dict))
# Output: {'colours': {'favorite': 'yellow'}}

### 12.2 OrderedDict ##################################################
#: OrderedDict keeps its entries sorted in the order that they are
#: initially inserted. Overwriting the value of an existing key doesn't
#: change the position of the key. However, deleting and reinserting an
#: entry moves the key to the end of the dictionary
colours = {
    'Red': 198,
    'Green': 170,
    'Blue': 160,
}

for key, value in colours.items():
    print(key, value)
# Output:
#   Green 170
#   Blue 160
#   Red 198
# Entries are retrieved in an unpredictable order

from collections import OrderedDict

colours = OrderedDict([
    ('Red', 198),
    ('Green', 170),
    ('Blue', 160),
])
for key, value in colours.items():
    print(key, value)
# Output:
#   Red 198
#   Green 170
#   Blue 160
# Entries are retrieved in an unpredictable order

### 12.3 counter ######################################################
#: Counter allows us to count the occurences of a particular item. For
#: instance it can be used to count the number of individual colours:
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)  # yapf: disable

favs = Counter(name for name, colour in colours)
print(favs)
# Output: Counter({
#    'Yasoob': 2,
#    'Ali': 2,
#    'Arham': 1,
#    'Ahmed': 1
# })

# Usable to count the most common lines in a file.
with open('dummy.txt', 'r') as f:
    line_count = Counter(f)
print(line_count)

### 12.4 deque ########################################################
#: deque provides you with a double ended queue which means that you
#: can append and delete elements from either side of the queue.
#: Double Ended QUEue -> D.E.QUE.
from collections import deque
d = deque()

# Similar to lists
d.append('1')
d.append('2')
d.append('3')
print(len(d))  # Output: 3
print(d[0])  # Output: 1
print(d[-1])  # Output: -1

# Can pop from both sides of the deque:
d = deque(range(5))
print(len(d))  # Output: 5

print(d.popleft())  # Output: 0
d.pop()  # Output: '4'
print(len(d))  # Output: '3'
print(d)  # Output: ['1', '2', '3']

#: You can also limit the amount of items it can hold. Trying to add an
#: item in excess of the limit will shove one off the opposite end.
d = deque(maxlen=30)

#: You can also expand the list in any direction with new values.
d = deque([1, 2, 3, 4, 5])
d.extendleft([0])
d.extend([6, 7, 8])
print(d)  # Output = deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

### 12.5 namedtuple ###################################################
#: You might already be acquainted with tuples. A tuple is basically a
#: immutable list which allows you to store a sequence of values
#: separated by commas. They are just like lists but have a few key
#: differences. The major one is that unlike lists, you can not
#: reassign an item in a tuple.

### regular tuple
man = ('Ali', 30)
print(man[0])  # Output: Ali

### named tuple
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'

#: You can also convert them to dictionaries
print(perry._asdict())

### 12.6 enum.Enum ####################################################
#: It allows the creation of pre-defined options that are addressable
#: via a primary key.
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alies.
    kitten = 1
    puppy = 2


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type=Species.cat)
drogon = Animal(name='Drogon', age=4, type=Species.dragon)
tom = Animal(name='Tom', age=75, type=Species.cat)
charlie = Animal(name='Charlie', age=2, type=Species.kitten)

# There are multiple ways to access enum
Species(1)
Species['cat']
Species.cat
