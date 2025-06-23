matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened List:", flattened)

# 2D list: 3 rows, 4 columns
two_D = [[0 for j in range(4)] for i in range(3)]
print("2D List:", two_D)

# 3D list: 3 layers, 4 rows, 5 columns
three_D = [[[0 for k in range(5)] for j in range(4)] for i in range(3)]
print("3D List:", three_D)
