class Person:
    def __init__(self):
        self.name = "Public"
        self._age = 25
        self.__salary = 50000


p = Person()
print(p.name)
print(p._age)
print(p._Person__salary)

# print(p.__salary)  # This will raise an AttributeError because __salary is private
# this is private and different from _age because it is name mangled
# name mangled means that it is not accessible directly outside the class
# print(p._Person__salary)  # This will work because we are accessing the mangled name
