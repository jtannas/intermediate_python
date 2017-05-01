"""
9. Mutation
The mutable and immutable datatypes in Python cause a lot of headache
for new programmers. In simple words, mutable means ‘able to be changed’
and immutable means ‘constant’.
"""

foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# Output: ['hi', 'bye']

#: Wait... What?
#: This happens because when assigning a variable to another variable
#: of a mutable datatype, any changes to the the data are reflected by
#: both variables.
#: Mutable datatypes are passed by reference instead of my value

def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]

#: This behaviour is because of the mutability o list. In Python, the
#: default arguments are evaluated at function definition, not at
#: function call. This can cause the function defaults to change when
#: you hadn't thought they would, causing bugs.

#: A better way to design that function is to use immutable defaults.
def add_to_revised(element, target=None):
    if target = None:
        target = []
    target.append(element)
    return target

add_to_revised(42)
# Output: [42]

add_to_revised(42)
# Output: [42]

add_to_revised(42)
# Output: [42]

#: Take home: be very careful when passing around mutable data. It's
#: likely to be changed in ways you did not expect.
#: Use tuples (immutable) as a default over lists, and a list when you
#: must.