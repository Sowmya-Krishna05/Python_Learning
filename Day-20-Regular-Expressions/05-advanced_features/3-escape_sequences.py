import re
text = "Price is $5.00"
print(re.findall(r"\$\d+\.\d{2}", text))

# uses \$ to escape the dollar sign
# and \d to match digits, \. to match the decimal point
# and \d{2} to match exactly two digits after the decimal point.
