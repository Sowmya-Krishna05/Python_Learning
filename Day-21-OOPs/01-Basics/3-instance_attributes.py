class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Alice")
p2 = Person("Bob")
print(p1.name, p2.name)
print(p1 is p2)  # False, different instances
print(p1.__dict__)
print(p2.__dict__)
