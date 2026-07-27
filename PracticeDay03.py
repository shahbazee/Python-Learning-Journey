# Create a function that prints "Hello, Python!"
def greet():
    print("Hello, Python!")


greet()


# Create a function that takes a name and prints Hello, <name>
def greet_name(name):
    print("Hello,", name)


greet_name("Shahbaz")


# Create a function that returns the length of a string
def string_length(text):
    return len(text)


result = string_length("Python")
print(result)


# Write a function to check whether a string is empty
def is_empty(text):
    if text == "":
        return True
    else:
        return False


print(is_empty(""))
print(is_empty("Python"))


# Count the number of consonants in a string
def count_consonants(text):
    count = 0

    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1

    return count


print(count_consonants("Hello Python"))


# Reverse a string using slicing
def reverse_string(string):
    print(string[::-1])


reverse_string("Python")


# Check whether a string is a palindrome
def palindrome_check(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


palindrome_check("Python")


# Convert a string to uppercase without using upper()


# File Operations

try:
    val1 = int(input("Enter a number: "))
    val2 = int(input("Enter another number: "))
    div = val1 / val2
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(f"The program not showing an error {div}")


try:
    fruits = ["apple", "banana", "cherry"]
    index = int(input("Enter an index: "))
    print(fruits[index])
except IndexError:
    print("Index out of range")
else:
    print(f"Fruit index is equal to index {index}")


user_input = input("Enter a string: ")

try:
    converted_string = int(user_input)
    print(f"String converted successfully: {converted_string}")
except ValueError:
    print("That's not a valid string!")


ages = {
    "Alice": 25,
    "Bob": 30
}

try:
    user_name = input("Enter a name: ")
    print(ages[user_name])
except KeyError:
    print("Name not found")

