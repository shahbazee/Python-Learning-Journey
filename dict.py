student = {
    "name" : "Shahbaz",
    "Field": "IT",
    "Location": "Lahore",
    "ZipCode": 54000
}

# Time complexity O(1)
keys = student.keys()
print(keys)

# Time Complexity 0(1)
values = student.values()
print(values)

# Time Complexity O(1)
items = student.items()
print(items)

# Time complexity O(1)
x = student.get("ZipCode")
print(x)

# Time Complexity is O(1)
y = student.pop("ZipCode")
print(y)

# Time complexity of Single update is O(1)
student.update({"Location": "Islamabad"})
print(student)

