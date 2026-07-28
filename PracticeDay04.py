marks = {
    "Ali": 25,
    "Ahmad": 44,
    "Hassan": 56,
    "Usama": 44,
    "Fawad": 55,
    "Rehan": 54,
    "Mudasir": 33,
    "Arish": 88,
    "Nouman": 99,
    "Tahir": 88
}

print(marks.clear())

fruits = {
    "Apple": 4,
    "Mango":  5,
    "Orange": 4,
    "Banana": 3
}

new = fruits.copy()
print(new)


list = ["Apple", "Mango", "Orange", "Banana"]

fruits_basket = dict.fromkeys(list)
print(fruits_basket)


required_marks = marks.get("Tahir")
print(required_marks)

student = {
    "name": "Shahbaz",
    "age": 24,
    "course": "Python"
}


# 2. items()
print("\nDictionary Items:")
for key, value in student.items():
    print(key, ":", value)

# 3. copy()
student_copy = student.copy()
print("\nCopied Dictionary:")
print(student_copy)

# 5. clear()
student_copy.clear()
print("\nAfter clear():")
print(student_copy)
