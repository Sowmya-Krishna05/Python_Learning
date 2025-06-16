data = {"a": 1, "b": 2}
print(data.keys())  # Returns a list containing the dictionary's keys
print(data.values())  # Returns a list of all the values in the dictionary
print(data.items())  # Returns a list containing tuple for each key value pair
print(data.get("a", 0))  # Returns the value of the specified key
data.pop("b")  # Removes the element with the specified key
print(data)
