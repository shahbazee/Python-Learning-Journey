from datetime import datetime, timedelta

now = datetime.now()

print("Current Date & Time:", now)

print("Tomorrow:", now + timedelta(days=1))

print("Current Year:", now.year)