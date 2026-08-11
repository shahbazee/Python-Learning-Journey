# Problem 1
from collections import Counter

text = "python programming"

counter = Counter(text)

print(counter)


#Problem 2
from collections import Counter

words = ["python", "sql", "python", "java", "sql", "python"]

counter = Counter(words)

print(counter)
print(counter.most_common(1))

#Problem 3

from collections import Counter

store1 = ["apple", "banana", "apple", "orange"]
store2 = ["apple", "banana", "banana", "mango"]

counter1 = Counter(store1)
counter2 = Counter(store2)

if counter1 == counter2:
    print("They are equal")
else:
    print("They are not equal")

