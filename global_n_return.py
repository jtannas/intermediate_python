"""
8. Global & Return
"""
### 8.0 GLOBALS #######################################################
def add(value1, value2):
    """Add two values and return the result"""
    return value1 + value2

result = add(3, 5)
print(f"Result 1 is {result}")
# Output: 8

#: Return is a keyword that hands-back a value from a function, exiting
#: the function in the process.
#: Here, it is assigned to the 'result' variable. In this case, result
#: is a global variable - a variable that can be accessed from outside
#: the scope of a function or class. They are usually declared in the
#: module namespace, but it is possible to make global variables inside
#: functions.

def add2(value1, value2):
    """Add two values and create a global named result2 with the result"""
    global result2
    result2 = value1 + value2

add2(2, 4)
print(f"Result 2 is {result2}")

#: In practice, using globals is a bad practice as it makes it very
#: to understand where variables are coming from.

### 8.1 MULTIPLE RETURN VALUES ########################################

# option 1: globals - obvious but awful
def profile1():
    global name1
    global age1
    name1 = 'Danny'
    age1 = 31

profile1()
print(name1)  # Output: Danny
print(age1)  # Output: 31


# option 2: packed tuples
def profile2():
    name2 = 'Also Danny'
    age2 = 32
    return (name2, age2)

profile_data2=profile2()
print(profile_data2[0])
print(profile_data2[1])


# option 3: tuple unpacking
def profile3():
    name3 = 'Danny the 3rd'
    age3 = 33
    return name3, age3

profile_name3, profile_age3 = profile3()
print(profile_name3)
print(profile_age3)


# option 4: named tuples
from collections import namedtuple
def profile4():
    my_profile = namedtuple('profile', ['name', 'age'])
    my_profile.name = 'Danny the 4th'
    my_profile.age = 34
    return my_profile

person = profile4()
print(person.name)
print(person.age)
