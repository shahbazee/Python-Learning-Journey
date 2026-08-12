import os

# Current directory
print(os.getcwd())

# Files/folders list
print(os.listdir())

# Create folder
if not os.path.exists("data"):
    os.mkdir("data")

# Create file path
file_path = os.path.join("data", "user.json")
print(file_path)

# Check if file exists
print(os.path.exists(file_path))
