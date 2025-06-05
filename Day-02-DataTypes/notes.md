# Day 2: Python Data Types – Summary

## 🔤 Strings

- Created using `' '`, `" "`, or `''' '''`.
- Immutable sequences of characters.

**Examples:**
text = "Python"
print(text[0])        # P
print(text[1:4])      # yth
print(text.upper())   # PYTHON
print(f"Hello {text}")  # Hello Python

## 🔢 Numbers

### ✅ Types
- **Integers**: int — `1, 0, -5`
- **Floating-point**: float — `3.14, -2.0`
- **Complex**: complex — `2 + 3j`

### 🔹 Arithmetic Operations
```python
a, b = 5, 2
print(a + b, a - b, a * b, a / b, a ** b, a // b, a % b)
```

### 🔹 Type Conversion
**Examples:**
int("5"), float("3.14"), str(25)

### 🔹 Math Functions
- `abs()`, `round()`, `pow()`, `divmod()`
- `math.sqrt()`, `math.ceil()`, `math.floor()`

### 🔹 Random Numbers
```python
import random
random.randint(1, 10)
random.choice([1, 2, 3])
