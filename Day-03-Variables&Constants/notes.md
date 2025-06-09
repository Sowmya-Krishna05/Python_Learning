# 📘 Day 03: Variables and Constants in Python

## 🔹 What is a Variable?
A **variable** is a name that refers to a value stored in memory. Python is **dynamically typed**, meaning you don’t have to declare the type explicitly.

```python
x = 5       # integer
name = "Ana" # string
pi = 3.14   # float
```

## 🔹 Dynamic Typing
Python automatically detects the variable type.

```python
x = 10       # int
x = "hello"  # now a str
x = 3.14     # now a float
```

## 🔹 Variable Naming Rules
✅ Valid:
- `name`, `user_name`, `userName`, `UserName`

❌ Invalid:
- `1name` (can't start with number)
- `user-name` (no special characters except `_`)
- `class`, `def` (reserved keywords)


## 🔹 Multiple Assignment
Assign values to multiple variables in one line.

```python
a, b, c = 1, 2, 3
x = y = z = 0
```

## 🔹 Variable Scope
- **Local Variable**: Declared inside a function.
- **Global Variable**: Declared outside all functions.


## 🔹 Constants in Python
Python doesn’t have true constants, but **uppercase naming** is used by convention.

```python
PI = 3.14159
GRAVITY = 9.8
```

Note: These values can still be changed, but should not be.


## 🧠 Key Takeaways
- Python is dynamically typed.
- Use descriptive and meaningful variable names.
- Constants should be declared in uppercase.
- Understand the difference between local and global scope.
