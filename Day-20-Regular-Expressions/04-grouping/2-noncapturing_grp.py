import re
text = "cat bat mat"
print(re.findall(r"(?:c|m)at", text))

# uses (?:...) to group without capturing
