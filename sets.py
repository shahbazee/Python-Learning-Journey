zipcode = {5400, 6400, 5000, 6000}

zipcode.remove(5000)
print(zipcode)

# Time complexity O(1)
x = zipcode.pop()
print(x)
print(zipcode)

zipcode.add(4000)
print(zipcode)

x = zipcode.clear()
print(x)