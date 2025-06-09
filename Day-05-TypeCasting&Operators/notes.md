# 📘 Day 5: Type Casting & Operators

## 🔁 **1. Type Casting (Type Conversion)**

Type casting means converting one data type into another.

**Two types:**
- **Implicit Casting** – Python automatically converts the type.
- **Explicit Casting** – You manually convert the type using functions like `int()`, `float()`, `str()`, etc.

**Examples:**
```python
# Implicit casting
x = 10
y = 2.5
z = x + y  # Result will be float
print(z, type(z))

# Explicit casting
a = "42"
b = int(a)
print(b, type(b))
```

## ➕ **2. Arithmetic Operators**

Used to perform basic mathematical operations.
operators: '+', '-', '*', '/', '//', '%', '**'.
**Example:**
```python
a = 10
b = 3
print(a + b, a ** b, a // b)
```

## ⚖️ **3. Comparison Operators**

Used to compare two values.
operators : '==', '!=', '>', '<', '>=', '<='.
**Example:**
```python
x = 5
y = 10
print(x == y, x < y)
```

## 🔗 **4. Logical Operators**

Used to combine multiple conditions.

| Operator | Description      |
|----------|------------------|
| `and`    | True if both are true |
| `or`     | True if at least one is true |
| `not`    | Inverts the condition |

**Example:**
```python
a = True
b = False
print(a and b, a or b, not a)
```

## 🧮 **5. Bitwise Operators**

Used for operations on binary numbers.
operators: 
            & - AND
            | - OR
            ^ - XOR
            ~ - NOT
            << - Left Shift
            >> - Right Shift

**Example:**
```python
a = 5   # 0101
b = 3   # 0011
print(a & b, a | b, a << 1)
```

## 📝 **6. Assignment Operators**

Used to assign values and perform operations simultaneously.

| Operator | Example     |
|----------|-------------|
| `=`      | a = 5       |
| `+=`     | a += 3      |
| `-=`     | a -= 2      |
| `*=`     | a *= 2      |
| `/=`     | a /= 2      |
| `//=`    | a //= 2     |
| `**=`    | a **= 2     |
| `%=`     | a %= 2      |

**Example:**
```python
x = 4
x *= 5
print(x)
```