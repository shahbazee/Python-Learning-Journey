import re

#Problem 1
text = "Python is powerful"

result = re.match(r"Python", text)

print(result.group())


#Problem 2
text = "Python is easy. Python is powerful."

result = re.findall("Python", text)

print(result)


#Problem 3
text = "I am learning Python"

result = re.search("Python", text)

print(result.group())