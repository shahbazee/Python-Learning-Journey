numbers = range(1, 6)

print(list(numbers))

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

print(list(map(lambda x: x * 2, range(5))))

print(all([True, True, True]))
print(any([False, False, True]))

print(sorted([5, 1, 3, 2]))

print(list(filter(lambda x: x % 2 == 0, range(10))))