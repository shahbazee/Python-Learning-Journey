from collections import Counter, deque

text = ["apple", "banana", "apple", "orange", "banana"]

counter = Counter(text)

print(counter)

queue = deque()

queue.append("Ali")
queue.append("Sara")
queue.append("Ahmed")

print(queue)

queue.popleft()

print(queue)