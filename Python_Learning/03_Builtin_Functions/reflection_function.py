class Student:

    college = "PU"

    def __init__(self):
        self.name = "Ali"

obj = Student()

print(dir(obj))

print(hasattr(obj, "name"))

print(getattr(obj, "name"))

setattr(obj, "age", 22)

print(obj.age)

delattr(obj, "age")

print(vars(obj))

print(globals().keys())

print(locals())