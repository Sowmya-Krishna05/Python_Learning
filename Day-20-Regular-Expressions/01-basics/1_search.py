import re
text_1 = "This year is 2025."
text_2 = "This is Sample Text."
match_1 = re.search(r"\d+", text_1)
match_2 = re.search(r"\bSample\b", text_2)
print("Match 1:", match_1.group() if match_1 else "No match found.")
print("Match 2:", match_2.group() if match_2 else "No match found.")

# re - Regular Expressions
# re.search() - Searches the string for a match and returns a match object if found.
