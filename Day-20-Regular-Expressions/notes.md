# Day 20: Regular Expressions

## What are Regular Expressions?
- Patterns used to match character combinations in strings.
- Useful for searching, validating, and manipulating text.

## Basic Syntax
- `.` : Any character except newline
- `^` : Start of string
- `$` : End of string
- `*` : 0 or more repetitions
- `+` : 1 or more repetitions
- `?` : 0 or 1 repetition
- `[]` : Set of characters
- `|` : OR operator
- `()` : Grouping

## Common Functions in Python (`re` module)
- `re.match()` : Checks for a match at the beginning of a string
- `re.search()` : Searches for a match anywhere in the string
- `re.findall()` : Returns all non-overlapping matches
- `re.sub()` : Replaces matches with a string

## Example
```python
import re

pattern = r"\d{3}-\d{2}-\d{4}"
text = "My number is 123-45-6789."
result = re.search(pattern, text)
if result:
    print("Found:", result.group())
```

## Tips
- Use raw strings (`r"pattern"`) to avoid escape issues.

