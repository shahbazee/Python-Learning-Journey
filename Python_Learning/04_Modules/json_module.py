import json

student = {
    "name": "Ali",
    "age": 22,
    "city": "Lahore"
}

json_data = json.dumps(student, indent=4)

print(json_data)

python_data = json.loads(json_data)

print(python_data["name"])