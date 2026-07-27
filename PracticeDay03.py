# Functions and String Practice

# Problem Number 01
# Crate a function that print a "Hello, Python!"
def print_string():
    print("Hello, Pyhton!")
print_string()


#Create a function that takes a name and prints Hello, <name>.
def print_name(name):
    print(f"Hello, {name}")

print_name("Ali")

# Create a function that returns the length of a string.
def string_length(string):
    print(len(string))

string_length("University of the Punjab")

#Write a function to check whether a string is empty.
def string_check(string):
    if len(string) == 0:
        print("String is empty")
    else:
        print(f"Available string. {string}")

string_check("Hello")


#Count the number of consonants in a string

def consonants_count(string):
    lower_sting = string.lower()
    counter = 0
    vowel_words = "aeiou"
    for characters in lower_sting:
        if characters.isalpha() and characters not in vowel_words:
            counter += 1
    print(f"The total Consonants in string are {counter}")

consonants_count("Shahbaz")




