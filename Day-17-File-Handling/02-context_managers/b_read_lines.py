# Read the file line by line
with open("example.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # Print each line without extra newline characters
