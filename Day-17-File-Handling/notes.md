# Day 17: File Handling in Python

## What is File Handling?
File handling allows you to read, write, and manipulate files (text, binary, etc.) on your system using Python.

## Opening Files

```python
file = open('filename.txt', 'mode')
```
- Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'b'` (binary), `'+'` (read/write)

## Reading Files

```python
with open('file.txt', 'r') as f:
    content = f.read()        # Reads entire file
    line = f.readline()       # Reads one line
    lines = f.readlines()     # Reads all lines into a list
```

## Writing Files

```python
with open('file.txt', 'w') as f:
    f.write('Hello, World!\n')
```
- `'w'` overwrites, `'a'` appends.

## Closing Files

- Use `with` statement to auto-close files.
- Or call `file.close()` manually.

## Example: Copying a File

```python
with open('source.txt', 'r') as src, open('dest.txt', 'w') as dst:
    for line in src:
        dst.write(line)
```

## Tips

- Always handle exceptions using `try...except`.
- Use `os` and `shutil` modules for advanced file operations.

## Useful Functions

- `os.remove('file.txt')` – Delete a file
- `os.rename('old.txt', 'new.txt')` – Rename a file
- `os.path.exists('file.txt')` – Check if file exists

## Working with JSON Files
- Use the `json` module to read and write JSON data.

```python
import json

# Writing JSON
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading JSON
with open('data.json', 'r') as f:
    data = json.load(f)
```

## Working with CSV Files

- Use the `csv` module to handle CSV files.

```python
import csv

# Writing CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 25])

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## Resources

- [Python File Handling Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python: Reading and Writing Files](https://realpython.com/read-write-files-python/)