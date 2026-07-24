# Program No 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number: ", largest)

# Program No 2
values = [2, 4, 3, 4, 3, 4, 3, 4]

require = 3
counter = 0
for i in values:
    if i == require:
        counter += 1

print("The value of counter:", counter)

# Program No 3
numbers2 = [1,2,3,4,5,5,5]

unique_numbers = list(dict.fromkeys(numbers2))

print(unique_numbers)


# Program No 4
numbers3 = [1, 3, 4, 5]

Total = 0
for num in numbers3:
    sum += num
print(sum)

