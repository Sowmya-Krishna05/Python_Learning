# Day 19: Iterators and Generators

## ✅ Iterators:
- Objects that implement `__iter__()` and `__next__()`
- Can be created manually or with custom classes

## ✅ Generators:
- Use `yield` to return values one at a time
- More memory-efficient and readable

## ✅ Generator Expressions:
- Like list comprehensions but with round brackets `()`
- Useful for lazy evaluation

## 🆚 Generator vs Iterator:
- Generators are iterators, but easier to write
- Iterators give you more control but are verbose

## ⚡ Use Case:
- Reading large files
- Streaming data
- Lazy loading
 