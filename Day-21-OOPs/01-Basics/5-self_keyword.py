class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")


d = Dog("Shitzu")
d.bark()
