"""
Python String Implementation
"""

text = "python programming"

# upper()
print(text.upper())

# lower()
print(text.lower())

# title()
print(text.title())

# capitalize()
print(text.capitalize())

# replace()
print(text.replace("python", "Java"))

# split()
print(text.split())

# join()
words = ["I", "Love", "Python"]
print(" ".join(words))

# find()
print(text.find("program"))

# startswith()
print(text.startswith("python"))

# endswith()
print(text.endswith("ing"))

# strip()
print("  Hello  ".strip())

# count()
print(text.count("m"))