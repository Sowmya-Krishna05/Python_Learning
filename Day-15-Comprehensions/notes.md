# Day 15: Comprehensions in Python

Comprehensions provide a concise way to create sequences like lists, dictionaries, sets, etc., using a single line of code.


## 🔹 1. List Comprehension
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

## 🔹 2. Dictionary Comprehension
```python
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## 🔹 3. Set Comprehension
```python
nums = [1, 2, 2, 3, 4, 4, 5, 6]
evens = {x for x in nums if x % 2 == 0}
print(evens)  # Output: {2, 4, 6}
```

## 🔹 4. Nested Comprehension
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
```

## 🔹 5. Conditional Comprehension
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']
```

✅ Use comprehensions to write clean, readable, and efficient Python code!