import re
text = "Heeellooo"
matches = re.findall(r"e{3,}", text)
print(matches)

# uses *, +, ?, {m,n} to match repeated patterns
