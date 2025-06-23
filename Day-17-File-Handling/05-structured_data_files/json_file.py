import json

# Write to a JSON file
data = {"name": "Charlie", "age": 28}
with open("data.json", "w") as file:
    json.dump(data, file)
# Read from a JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)  