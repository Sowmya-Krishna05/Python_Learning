# Demo of various modes
file = open("demo.txt", "w+")
file.write("Using w+ mode")
file.seek(10)  # Move the cursor to the 10th byte
print(file.read())
file.seek(0) 
print(file.read()) 
file.close()
