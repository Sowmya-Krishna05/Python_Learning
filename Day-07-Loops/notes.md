# Day 7 — Loop Control Statements in Python
Python provides three powerful statements to control the flow inside loops:

## 🔁 1. `break`
- Immediately exits the loop.
- Used when a certain condition is met and we no longer need to continue looping.

## 🔄 2. `continue`
- Skips the current iteration and jumps to the next.
- Used when you want to skip a specific condition inside the loop.

## 🧘‍♂️ 3. `pass`
- A placeholder that does nothing.
- Useful when a statement is syntactically required but you don’t want any code to execute yet.
**Example:**
```python
for i in range(3):
    if i == 1:
        pass
    print(i)
```
**Output:** `0 1 2`

## 4. Using `else` with Loops

You can attach an `else` block to `for` and `while` loops, which executes only if the loop **was not broken** with `break`.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed normally")
```
