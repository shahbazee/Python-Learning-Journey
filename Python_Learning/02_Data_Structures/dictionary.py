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