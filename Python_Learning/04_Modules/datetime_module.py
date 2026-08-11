from datetime import datetime

now = datetime.now()

print(now)


# Problem 2
today = datetime.now()

future = today + timedelta(days=7)

print(future)

# Problem 3
date1 = datetime(2026, 8, 11)
date2 = datetime(2026, 8, 20)

difference = date2 - date1

print(difference.days)

# Problem 4
date = "11-08-2026"

result = datetime.strptime(date, "%d-%m-%Y")

print(result)