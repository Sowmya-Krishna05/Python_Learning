import re
text = "start middle end"
print(re.findall(r"^start", text))
print(re.findall(r"end$", text))

# uses ^ and $ to match beginning and end of strings
