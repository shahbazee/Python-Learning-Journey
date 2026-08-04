import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    users = response.json()

    for user in users[:3]:
        print(user["name"])