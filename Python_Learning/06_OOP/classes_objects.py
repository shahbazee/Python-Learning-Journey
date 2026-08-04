class Student:
    """Represents a student."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old.")


# Object Creation
student1 = Student("Ali", 22)
student2 = Student("Sara", 21)

student1.introduce()
student2.introduce()