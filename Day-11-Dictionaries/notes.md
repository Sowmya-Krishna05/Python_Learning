# 🗂 Day 11: Python Dictionaries - Detailed Notes

## 🔑 1. Dictionary Basics
- Dictionary is a collection of key-value pairs.
- Defined using `{}` with colon `:` separating key and value.
```python
student = {"name": "Alice", "age": 21}
```

## 🧪 2. Dictionary Methods
- `.keys()`, `.values()`, `.items()` for accessing keys/values.
- `.get(key, default)` returns value or default if key not found.
- `.pop(key)` removes a key.

## 🔄 3. Looping through Dictionary
```python
for key, value in my_dict.items():
    print(key, value)
```
## 🧱 4. Nested Dictionaries
- Dictionaries within dictionaries for structured data.
```python
users = {
    "user1": {"name": "Tom", "age": 22},
    "user2": {"name": "Jerry", "age": 24}
}
```
## ⚙️ 5. Dictionary Comprehension
- Create dictionaries in one line:
```python
squares = {x: x**2 for x in range(5)}
```
## 🧩 6. `fromkeys()` Method
- Create dictionary from a list of keys with default value:
```python
dict.fromkeys(["a", "b"], 0)
```

## 🧪 7. `setdefault()` Method
- Sets default value if key doesn’t exist:
```python
profile.setdefault("age", 30)
```