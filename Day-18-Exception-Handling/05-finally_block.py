try:
    print("Try block. This is where you put code that might raise an exception.")
finally:
    print("Finally block. This code runs no matter what, even if an exception occurs.")


# Example of using finally with a file operation
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals():
        file.close()
