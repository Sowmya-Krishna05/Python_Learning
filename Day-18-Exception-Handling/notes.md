# Day 18: Exception Handling
**Subtopics:**
1. Basic try-except
2. Multiple except blocks
3. Generic exception handling
4. else clause
5. finally block
6. Raising exceptions
7. Custom exceptions
8. Nested try-except
9. Exception with traceback

## 1. Basic try-except

Use `try-except` to catch and handle specific errors, preventing your program from crashing.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
*Note: The code inside `try` raises a `ZeroDivisionError`, which is caught and handled by the `except` block.*

## 2. Multiple except blocks

Handle different types of exceptions separately for more precise error management.
*Note: The code tries to convert a non-numeric string to an integer, raising a `ValueError`.*

## 3. Generic exception handling

Catch any exception using the base `Exception` class, useful for logging or debugging.
```python
try:
    open("file.txt")
except Exception as e:
    print(f"An error occurred: {e}")
# Output: An error occurred: [Errno 2] No such file or directory: 'file.txt'
```
*Note: This approach catches all exceptions, but use it carefully to avoid hiding bugs.*

## 4. else clause

The `else` block runs if no exceptions occur in the `try` block.
*Note: `else` is useful for code that should only run if the `try` block succeeds.*

## 5. finally block

The `finally` block always runs, whether or not an exception occurred.
*Note: Use `finally` for cleanup actions like closing files or releasing resources.*

## 6. Raising exceptions

Manually raise exceptions to signal errors in your own code.
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
set_age(-1)
# Output: ValueError: Age cannot be negative.
```
*Note: Raising exceptions helps enforce correct usage of your functions.*

## 7. Custom exceptions

Define your own exception classes for more descriptive error handling.
```python
class MyError(Exception):
    pass

raise MyError("Something went wrong!")
# Output: MyError: Something went wrong!
```
*Note: Custom exceptions make your code easier to debug and maintain.*

## 8. Nested try-except

Nest `try-except` blocks to handle errors at different levels.
*Note: The inner exception is handled without propagating to the outer block.*

## 9. Exception with traceback

Use the `traceback` module to print detailed error information for debugging.
```python
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc()
```
*Note: Tracebacks help identify where and why an error occurred.*
