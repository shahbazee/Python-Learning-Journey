class Parent:

    @classmethod
    def cls_method(cls):
        print(cls)

    @staticmethod
    def st_method():
        print("Static Method")

    @property
    def info(self):
        return "Property"

class Child(Parent):
    pass

obj = Child()

print(obj.info)

obj.cls_method()

obj.st_method()

print(isinstance(obj, Parent))

print(issubclass(Child, Parent))