import json

user = {
    "name": "Shahbaz",
    "age": 24,
    "skills": ["Python", "SQL"]
}

# Python dictionary → JSON string
json_data = json.dumps(user)
print(json_data)

# JSON string → Python dictionary
data = json.loads(json_data)
print(data["name"])

# Dictionary → JSON file
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

# JSON file → Python dictionary
with open("user.json", "r") as file:
    data = json.load(file)

print(data)