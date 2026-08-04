def outer(message):
    def inner():
        print(message)
    return inner

greet = outer("Hello, Python!")

greet()


def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15