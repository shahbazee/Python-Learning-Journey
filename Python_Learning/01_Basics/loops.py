# even_counter = 0
# odd_counter = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#      even_counter = even_counter + 1
#     elif i % 2 != 0:
#      odd_counter = odd_counter + 1
#
# print(f"Even Number = {even_counter}")
# print(f"Odd Number = {odd_counter}")


numbers = [2, 3, 5, 6, 9, 10, 12, 15, 35, 16, 1, 18, 10, 10,  20, 21, 24, 25, 27, 30, 31, 34, 36, 38]
target = int(input("Enter a target number: "))
new_list = []
for num in numbers:
    for num2 in numbers:
        if num + num2 == target:
            new_list.append([num, num2])


print(new_list)