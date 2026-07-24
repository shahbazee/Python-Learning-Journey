marks = [23, 33,44,22, 22, 33]
print(marks)


# Time complexity of inserting in list is O(n)
marks.insert(0,23)
print(marks)

# Time complexity is O(1)
marks.append(00)
print(marks)

#Time Complexity is O(n)
x = marks.count(22)
print(x)

#Time complexity is O(n)
marks.sort()
print(marks)

# time complexity is O(n)
marks.reverse()
print(marks)

# Time complexity is O(1)
x = marks.pop(3)
print(x)