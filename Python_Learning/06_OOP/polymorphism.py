
class Bird:

    def sound(self):
        print("Bird makes a sound.")


class Sparrow(Bird):

    def sound(self):
        print("Sparrow chirps.")


class Parrot(Bird):

    def sound(self):
        print("Parrot talks.")


def make_sound(bird):
    bird.sound()


sparrow = Sparrow()
parrot = Parrot()

make_sound(sparrow)
make_sound(parrot)