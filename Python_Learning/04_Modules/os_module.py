import os

print("Current Working Directory:")
print(os.getcwd())

print("\nFiles in Current Directory:")
print(os.listdir())

folder = "demo_folder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"{folder} created.")

print("Operating System:", os.name)