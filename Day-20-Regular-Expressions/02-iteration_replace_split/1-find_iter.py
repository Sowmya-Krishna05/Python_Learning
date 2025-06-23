import re
text = "123 456 789"
for match in re.finditer(r"\d+", text):
    print("Match at", match.span(), ":", match.group())
