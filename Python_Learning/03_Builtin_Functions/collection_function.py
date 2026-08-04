items = ["Python", "Java", "C++"]

print(len(items))

for index, value in enumerate(items):
    print(index, value)

names = ["Ali", "Sara"]
ages = [20, 22]

print(list(zip(names, ages)))

print(list(reversed(items)))

print(items[slice(0, 2)])