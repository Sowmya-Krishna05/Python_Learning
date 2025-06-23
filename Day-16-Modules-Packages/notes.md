# 📘 Day 16: Modules and Packages

Python modules and packages help organize code logically and reuse functionality across projects.

## 🔹 1. What is a Module?

A **module** is any Python file (`.py`) that contains code: functions, classes, or variables. It allows you to break your program into smaller, reusable files.

**Example (built-in module):**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

**Example (custom module):**
```python
def greet(name):
    return f"Hello, {name}!"

# File: custom-module-example.py
import custom_module
print(custom_module.greet("Alice"))  # Output: Hello, Alice!
```

## 🔹 2. What is a Package?

A **package** is a collection of related Python modules organized in directories that contain an `__init__.py` file.

📁 Example structure:
```
package-demo/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

**Using a package:**
```python
from package_demo import math_utils, string_utils

print(math_utils.add(2, 3))         # Output: 5
print(string_utils.shout("hello"))  # Output: HELLO!
```

## 🔹 3. `__init__.py` Explained

- Marks a folder as a Python package.
- Can contain initialization code.
- Required for compatibility with older Python versions.

## 🔹 4. Relative vs Absolute Imports

✅ **Absolute Import** – full path from the project root:
```python
from package_demo import math_utils
```

🔄 **Relative Import** – relative to the current module (used inside packages):
```python
from . import math_utils
```

## 🔹 5. Why Use Modules & Packages?

- Code reusability
- Clean organization
- Maintainability
- Scalable architecture