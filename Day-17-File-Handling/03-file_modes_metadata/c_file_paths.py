# Construct file paths using os.path
import os
path = os.path.join("file.txt")
print("Constructed path:", path)
print("Absolute Path:", os.path.abspath(path))
print("Exists?", os.path.exists(path))
print("File Name:", os.path.basename(path))
