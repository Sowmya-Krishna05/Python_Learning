# Day 9: Tuples in Python
Tuples are ordered, immutable sequences in Python. They are useful when you want to store a collection of values that should not change.

## 📌 1. Tuple Creation

```python
t1 = (1, 2, 3)
t2 = tuple([4, 5])
t3 = "a", "b", "c"  # Implicit tuple
```

## 📌 2. Tuple Indexing & Slicing

```python
t = ('x', 'y', 'z', 'w')
print(t[0])     # Output: 'x'
print(t[-1])    # Output: 'w'
print(t[1:3])   # Output: ('y', 'z')
```

## 📌 3. Tuple Immutability

Tuples **cannot be changed** after creation.

```python
t = (10, 20, 30)
# t[1] = 50  ❌ This will raise TypeError
```

## 📌 4. Tuple Packing & Unpacking

```python
# Packing
student = ("Smith", 22, "CSE")

# Unpacking
name, age, branch = student
print(name)   # Smith
```

## 📌 5. Nested Tuples

Tuples can hold other tuples.

```python
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3
```

## 📌 6. Tuple with One Element (Singleton)

Always include a comma!

```python
single = (5,)
not_tuple = (5)
print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>
```

## 📌 7. Iterating Through Tuples

```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
```

## 📌 8. Tuple Methods

```python
t = (1, 1, 2, 3)
print(t.count(1))  # 2
print(t.index(3))  # 3
```

## 📌 9. Tuples vs Lists

| Feature      | Tuple            | List           |
|--------------|------------------|----------------|
| Mutability   | Immutable        | Mutable        |
| Syntax       |  (1, 2)          |  [1, 2]        |
| Performance  | Faster           | Slightly slower|
| Use Case     | Fixed structure  | Dynamic data   |


## 📌 10. Tuple Use Cases

- Function return values
- Dictionary keys (if hashable)
- Safer data containers than lists
```python
def info():
    return "John", 25, "Engineer"

print(info)  # ('John', 25, 'Engineer')
```

📝 **Tip:** Use tuples when:
- The data should not change.
- You want to use the data as dictionary keys.
- You need better performance than lists.
