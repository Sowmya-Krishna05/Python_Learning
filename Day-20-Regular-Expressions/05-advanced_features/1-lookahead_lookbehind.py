import re
text = "python3 python2 python"
print(re.findall(r"python(?=3)", text))

# the code searches the text string for all instances of the word "python" that are immediately followed by the number 3.
# the lookahead assertion (?=3) checks for the presence of 3 after "python" without including it in the match.
print(re.findall(r"(?<=python)3", text))
