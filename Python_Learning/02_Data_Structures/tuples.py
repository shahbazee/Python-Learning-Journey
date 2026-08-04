"""
Python Tuple Implementation
"""

student = ("Ali", 22, "Lahore", "Python")

# count()
print(student.count("Ali"))

# index()
print(student.index("Python"))

# Traversing
for item in student:
    print(item)

# Slicing
print(student[:2])

# Packing
data = 10, 20, 30

# Unpacking
a, b, c = data
print(a, b, c)

# Membership
print("Ali" in student)

# Length
print(len(student))

# Concatenation
new_tuple = student + ("Developer",)

print(new_tuple)