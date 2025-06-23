import re
text = "ID: 123, Code: 456, Zip: 789"
print(re.findall(r"\d+", text))
