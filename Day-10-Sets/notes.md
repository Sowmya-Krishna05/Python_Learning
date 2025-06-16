# Day 10: Sets in Python
Sets are unordered, mutable (changeable), and do not allow duplicate values.

## ✅ 1. Creating Sets
```python
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

## 🔁 2. Set Operations
- **Union**: Combines elements from both sets
- **Intersection**: Common elements
- **Difference**: Elements in one set but not the other
- **Symmetric Difference**: Elements in either set, but not both

## 🔗 3. Set Relationships
- **Subset**: `a.issubset(b)`
- **Superset**: `a.issuperset(b)`
- **Disjoint**: `a.isdisjoint(b)`

## ✍️ 4. Modifying Sets
- `add()`: Add a single item
- `remove()` / `discard()`: Remove item
- `update()`: Add multiple items

## ❄️ 5. Frozen Sets
Immutable sets – elements cannot be changed after creation.
Sets are useful when you want to eliminate duplicates and perform mathematical set operations efficiently.