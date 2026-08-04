
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):

    def speak(self):
        print(f"{self.name} says Meow!")


dog = Dog("Buddy")
cat = Cat("Kitty")

dog.speak()
cat.speak()