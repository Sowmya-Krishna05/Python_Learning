 # 📘 Day 14: Python String Methods

Strings are sequences of characters enclosed in single or double quotes. Python offers a rich set of built-in **string methods** to manipulate and analyze text data.

## 1. Case Conversion & Formatting (`1-case-format.py`)

- `upper()` – Converts all characters to uppercase.
- `lower()` – Converts all characters to lowercase.
- `capitalize()` – Capitalizes the first character.
- `title()` – Capitalizes the first character of each word.
- `swapcase()` – Swaps case (lowercase to uppercase and vice versa).
- `format()` – Used for string formatting.
- `f""` – Modern and cleaner string formatting method (f-strings).

## 2. Whitespace Removal & Alignment (`2-strip-align.py`)

- `strip()` – Removes leading and trailing whitespaces.
- `lstrip()` / `rstrip()` – Removes left or right whitespaces.
- `center(width, fillchar)` – Centers the string with padding.
- `ljust(width)`, `rjust(width)` – Left/right aligns the string.
- `zfill(width)` – Pads the string with zeros.

**Example:**
```python
text = "  hello  "
print(text.strip())          # "hello"
print("42".zfill(5))         # "00042"
```

## 3. Checking & Searching (`3-check-search.py`)

### Check Properties:
- `isalpha()` – Only alphabets
- `isdigit()` – Only digits
- `isalnum()` – Alphabets or digits
- `isspace()` – Only whitespace

### Searching:
- `find()`, `rfind()` – Finds substring (returns -1 if not found).
- `index()` – Like `find()` but throws error if not found.
- `startswith()`, `endswith()` – Check string prefixes/suffixes.

**Example:**
```python
text = "Python3"
print(text.isalnum())        # True
print(text.startswith("Py")) # True
```

## 4. Replace, Count, Split, Join (`4-replace-count-join.py`)

- `replace(old, new)` – Replaces substring.
- `count(sub)` – Counts substring occurrences.
- `split()` – Splits string by delimiter into a list.
- `join(iterable)` – Joins list elements into a single string.

**Example:**
```python
msg = "banana banana"
print(msg.count("a"))             # 6
print("-".join(["one", "two"]))  # one-two
```

## 5. Encoding & Line Splitting (`5-encode-splitlines.py`)

- `encode()` – Converts string into bytes (UTF-8 by default).
- `splitlines()` – Splits a multiline string at line breaks.

**Example:**
```python
s = "Hello\nWorld"
print(s.splitlines())     # ['Hello', 'World']
print("Data".encode())    # b'Data'
```
