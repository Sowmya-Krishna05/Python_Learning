import re
text = "Order 123: Done\nOrder 456: Pending\nOrder 789: Done"
print(re.compile(r"\d+").findall(text))
