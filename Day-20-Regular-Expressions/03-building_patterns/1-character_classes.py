import re
text = "A1 B2 C3"
print(re.findall(r"\w\d", text))

# uses \d, \w, \s, etc. to match character classes
