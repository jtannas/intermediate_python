"""5. set Data Structure

set is a really useful data structure. sets behave mostly like lists
with the distinction that they can not contain duplicate values. It is
really useful in a lot of cases. For instance you might want to check
whether there are duplicates in a list or not.
"""

some_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']

# The non-set way
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)  # Output: ['b', 'n']

# The set way
no_dups = set(some_list)
print(f"no_dups: {sorted(no_dups)}")

uniques = set(x for x in some_list if some_list.count(x) == 1)
print(f"uniques: {sorted(uniques)}")

duplicates = set(x for x in some_list if some_list.count(x) > 1)
print(f"dups: {sorted(duplicates)}")

# Set intersections
first_set = set(some_list)
other_set = set(['d', 'e', 'f', 'm'])
matched = other_set.intersection(first_set)
print(f"matched: {matched}")
unmatched = other_set.difference(first_set)
print(f"unmatched: {unmatched}")