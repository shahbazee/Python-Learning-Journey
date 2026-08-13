"""
Python List Implementation
"""

# Creation
fruits = ["Apple", "Banana", "Orange"]

# append()
fruits.append("Mango")

# extend()
fruits.extend(["Grapes", "Peach"])

# insert()
fruits.insert(1, "Kiwi")

# remove()
fruits.remove("Orange")

# pop()
removed = fruits.pop()

# index()
print("Index:", fruits.index("Banana"))

# count()
print("Count:", fruits.count("Apple"))

# sort()
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)

# copy()
copy_list = fruits.copy()

# clear()
temp = [1, 2]
temp.clear()

print(fruits)
print(copy_list)

#   Remove Duplicate

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)