class Bird:
    def fly(self):
        print("Bird can fly")


class Airplane:
    def fly(self):
        print("Airplane can fly")


def make_it_fly(flyable):
    flyable.fly()


make_it_fly(Bird())
make_it_fly(Airplane())
