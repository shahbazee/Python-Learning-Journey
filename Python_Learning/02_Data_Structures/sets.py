"""
Python Set Implementation
"""

numbers = {1, 2, 3, 4}

# add()
numbers.add(5)

# update()
numbers.update([6, 7])

# remove()
numbers.remove(2)

# discard()
numbers.discard(10)

# pop()
numbers.pop()

# union()
a = {1, 2}
b = {2, 3}

print(a.union(b))

# intersection()
print(a.intersection(b))

# difference()
print(a.difference(b))

# symmetric_difference()
print(a.symmetric_difference(b))

# copy()
copy_set = numbers.copy()

print(copy_set)