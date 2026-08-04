# Built-in Data Types

print(int("10"))
print(float("10.5"))
print(complex(2, 3))
print(bool(1))

print(str(123))

print(bytes("Hello", "utf-8"))
print(bytearray("Hello", "utf-8"))

data = bytearray(b"Python")
print(memoryview(data))

print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(frozenset([1, 2, 3]))
print(dict(name="Ali", age=22))