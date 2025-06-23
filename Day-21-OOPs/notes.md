# Day 21: OOPs Notes

## Object-Oriented Programming (OOP) Concepts

Object-Oriented Programming is a paradigm based on the concept of "objects", which can contain data and code to manipulate that data.

- **Class**: A blueprint for creating objects. Defines attributes and methods.
- **Object**: An instance of a class. Represents a specific entity with state and behavior.
- **Attributes**: Variables that store data about the object. Can be instance or class attributes.
- **Methods**: Functions defined inside a class that describe the behaviors of the object.

## Four Key Principles of OOP

1. **Encapsulation**
    - Bundles data (attributes) and methods that operate on the data into a single unit (class).
    - Restricts direct access to some of the object's components, usually by making attributes private or protected.
    - Example: Using getter and setter methods to access private attributes.

2. **Inheritance**
    - Allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).
    - Promotes code reuse and establishes a relationship between classes.
    - Example: A `Dog` class inheriting from an `Animal` class.

3. **Polymorphism**
    - Means "many forms". Allows objects of different classes to be treated as objects of a common superclass.
    - Achieved by method overriding (same method name, different implementation in subclasses).
    - Example: Different animals implementing their own version of a `speak()` method.

4. **Abstraction**
    - Hides complex implementation details and shows only the necessary features of an object.
    - Achieved using abstract classes and methods (with the `abc` module in Python).
    - Example: Defining an abstract `speak()` method in the `Animal` class.

## Example: OOP in Python

```python
class Animal:
     def __init__(self, name):
          self.name = name  # Attribute

     def speak(self):
          raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
     def speak(self):
          return f"{self.name} says Woof!"

class Cat(Animal):
     def speak(self):
          return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

## Additional Notes

- Use `self` to refer to the instance within class methods.
- The constructor method in Python is `__init__`.
- Use `super()` to call methods from the parent class.
- Private attributes are prefixed with `_` or `__` (e.g., `self._age`).
- Abstract classes can be created using the `abc` module for enforcing method implementation in subclasses.

## Summary Table

| Principle      | Description                                      | Example                |
| -------------- | ------------------------------------------------ | ---------------------- |
| Encapsulation  | Hides data, provides methods to access it        | Getters/Setters        |
| Inheritance    | Child class inherits from parent class           | `class Dog(Animal)`    |
| Polymorphism   | Same method, different implementations           | `speak()` in subclasses|
| Abstraction    | Hides complexity, shows only essentials          | Abstract methods       |

