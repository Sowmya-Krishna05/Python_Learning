class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):
    def greet(self):
        super().greet()  # Call the method from Parent
        print("Hello from Child")


c = Child()
c.greet()  # This will call the greet method from Child, which in turn calls Parent's greet method
