# Day 12: Function Basics in Python

Functions are reusable blocks of code designed to perform a specific task. This lesson covers how to define, call, and use functions effectively in Python.

## 🧠 1. Defining a Function [`define-function.py`]

```python
def greet():
    print("Hello!")
```
Defines a simple function called `greet` that prints a message when called.

## ▶️ 2. Calling a Function [`call-function.py`]

```python
def greet():
    print("Hello!")

greet()
```
Calling a function runs its code.

## 🎯 3. Function with Parameters [`function-parameters.py`]

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
Parameters allow a function to accept input.

## 🔁 4. Function with Return Value [`function-return.py`]

```python
def add(a, b):
    return a + b

print(add(3, 4))
```
Use `return` to output a value from the function.

## ⚙️ 5. Default Parameters [`default-params.py`]

```python
def greet(name="Guest"):
    print(f"Welcome, {name}")

greet()
greet("Sam")
```
Default parameters are used when no value is provided by the caller.

## 🗝️ 6. Keyword Arguments [`keyword-args.py`]

```python
def intro(name, age):
    print(f"{name} is {age} years old")

intro(age=25, name="Sam")
```
Arguments can be passed using keywords for clarity and flexibility.

## 🌍 7. Variable Scope 

```python
x = 10

def change():
    x = 5
    print("Inside function:", x)

change()
print("Outside function:", x)
```
Local variables are limited to the function scope, while global variables exist outside.

## 📝 8. Docstrings 

```python
def square(x):
    """Returns square of x"""
    return x * x

print(square(5))
```
Triple-quoted strings inside a function serve as documentation.

## ✅ Summary

- Use `def` to define a function.
- Use parameters and return values to make functions powerful.
- Default and keyword arguments provide flexibility.
- Understand the scope to avoid variable conflicts.
- Docstrings help others (and yourself) understand what the function does.