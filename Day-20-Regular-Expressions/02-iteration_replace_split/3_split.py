import re
text = "green,red;blue orange"
print(re.split(r'[ ,;]', text))
