import re
text = "Name: John, Age: 30"
match = re.search(r"Name: (\w+), Age: (\d+)", text)
if match:
    print("Name:", match.group(1), "Age:", match.group(2))

# uses () to capture groups in a match
