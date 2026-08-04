with open("sample.txt", "w") as file:
    file.write("Hello Python")

with open("sample.txt") as file:
    print(file.read())