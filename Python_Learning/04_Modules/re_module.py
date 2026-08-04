import re

text = "My email is shahbaz123@gmail.com"

pattern = r"\S+@\S+"

match = re.search(pattern, text)

if match:
    print("Email:", match.group())