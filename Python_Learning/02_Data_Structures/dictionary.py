"""
Python Dictionary Implementation
"""

student = {
    "name": "Ali",
    "age": 22,
    "city": "Lahore"
}

# get()
print(student.get("name"))

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# update()
student.update({"age": 23})

# pop()
student.pop("city")

# popitem()
student.popitem()

# setdefault()
student.setdefault("country", "Pakistan")

# copy()
copy_dict = student.copy()

# clear()
temp = {"a": 1}
temp.clear()

print(student)

# Count Frequency

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

# Two Sum Problem

nums = [2, 7, 11, 15]
target = 9

num_map = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in num_map:
        print([num_map[complement], i])
        break

    num_map[num] = i