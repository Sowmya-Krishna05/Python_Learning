# Day 13: Advanced Functions in Python
 Here's a breakdown of advanced function topics:

## 1. Default Arguments
You can provide default values to parameters.

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")
```

## 2. Positional and Keyword Arguments
You can pass arguments by position or by keyword.

```python
def info(name, age):
    print(f"{name} is {age} years old.")

info("Tom", 25)              # Positional
info(age=30, name="Jerry")   # Keyword
```

## 3. Variable-Length Arguments (*args)
Allows passing any number of positional arguments.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))
```

## 4. Keyword Variable-Length Arguments (**kwargs)
Allows passing any number of keyword arguments.

```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, city="Paris")
```

## 5. Lambda Functions
Anonymous one-line functions.

```python
square = lambda x: x * x
print(square(5))
```

## 6. Function as Argument
Functions can be passed as parameters to other functions.

```python
def apply(fn, value):
    return fn(value)

def double(x):
    return x * 2

print(apply(double, 4))
```

## 7. Return Function (Closures)
Functions can return other functions.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add = outer(5)
print(add(3)) 
```

## 8. Nested Functions
Functions defined inside other functions.