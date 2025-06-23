# Check if a file exists
import os
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")

# Check if a directory exists
if os.path.exists("sample_directory"):
    print("Directory exists")
else:
    print("Not found")