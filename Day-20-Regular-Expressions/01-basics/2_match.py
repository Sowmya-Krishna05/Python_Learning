import re
txt = "The rain in Spain"
x_1 = re.match(r"rain\d", txt)
x_2 = re.match(r".*rain", txt)
print("Match 1:", x_1.group() if x_1 else "No match found.")
print("Match 2:", x_2.group() if x_2 else "No match found.")
