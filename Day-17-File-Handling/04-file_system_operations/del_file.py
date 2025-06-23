import os
if os.path.exists("file1.txt"):
    os.remove("file1.txt")
    print("Deleted file1.txt")
else:
    print("File does not exist")