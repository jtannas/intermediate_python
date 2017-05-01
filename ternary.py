"""
6. Ternary Operators

Ternary operators are more commonly known as conditional expressions in
Python. These operators evaluate something based on a condition being
true or not. They became a part of Python in version 2.4
"""

# Modern Python Way.
def positive_test(num):
    return 'positive' if num > 0 else 'not positive'

print(f"1 is {positive_test(1)}")
print(f"-1 is {positive_test(-1)}")

# Pre Python 2.4 way - do not use - it evaluates all possibities.
num = 3
print(('not positive', 'positve')[num > 0])

print(':-)' if True else 1/0)
print((1/0, ':D')[True])
