import re
text = "Hello\nWorld\nHello\nPython"
print(re.findall(r"^\w+", text, re.MULTILINE))

# the code searches the text string for all instances of a word at the beginning of each line.
# the re.MULTILINE flag allows the ^ anchor to match the start of each line, not just the start of the entire string.
# uses flags like re.IGNORECASE, re.MULTILINE, etc.
