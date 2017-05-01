"""
15. Comprehensions
Comprehensions are a feature of Python which I would really miss if I
ever have to leave it. Comprehensions are constructs that allow
sequences to be built from other sequences. Three types of
comprehensions are supported in both Python 2 and Python 3:
    - list comprehensions
    - dictionary comprehensions
    - set comprehensions
We will discuss them one by one. Once you get the hang of using list
comprehensions then you can use any of them easily.
"""
### 15.1 LIST COMPREHENSIONS ##########################################
#: list comprehensions provide a short and concise way to create lists.
#: It consists of square brackets containing an expression followed by
#: a for clause, then zero or more for or if clauses. The expression
#: can be anything, meaning you can put in all kinds of objects in
#: lists. The result would be a new list made after the evaluation of
#: the expression in context of the if and for clauses.

#: Blueprint
#: variable = [out_exp for var in input_list if if_exp == 2]

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

squared = [x**2 for x in range(10)]

### 15.2 DICT COMPREHENSIONS ##########################################
mcase = {
    'a': 10,
    'b': 34,
    'A': 7,
    'Z': 3,
}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}  # totals the values from the uppercase and lowercase keys

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}

### 15.3 SET COMPREHENSIONS ###########################################
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}