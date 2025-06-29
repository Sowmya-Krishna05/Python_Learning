# Day 23: Context Managers in Python

## What are Context Managers?
Context managers allow you to allocate and release resources precisely when you want to. The most common way to use a context manager is with the `with` statement.

## Why Use Context Managers?
- Ensure resources are properly cleaned up (e.g., files, network connections)
- Make code cleaner and more readable

## Example: Using a File Context Manager
```python
with open('example.txt', 'r') as file:
    data = file.read()
# File is automatically closed here
```

## Creating a Custom Context Manager

### Using a Class
```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside context")
```

### Using a Generator and `contextlib`
```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    yield
    print("Exiting context")

with my_context():
    print("Inside context")
```

## Key Points
- Use context managers to manage resources safely.
- Implement with classes (`__enter__`, `__exit__`) or with `contextlib.contextmanager`.
- The `with` statement is the standard way to use context managers.