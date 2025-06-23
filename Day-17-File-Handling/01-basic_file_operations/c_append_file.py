# Append new content without deleting existing data
with open("example.txt", "a") as f:
    f.write("\nThis line is appended.")

with open("example.txt", "r") as f:
    print(f.read())

