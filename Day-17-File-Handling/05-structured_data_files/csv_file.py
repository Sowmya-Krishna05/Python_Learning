import csv

# Write to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 22])
    writer.writerow(["Bob", 30])

# Read from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV File Content:\n" + file.read())
