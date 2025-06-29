from contextlib import contextmanager


# This decorator allows us to define a context manager using a generator function
@contextmanager
def open_file(file, mode):
    f = open(file, mode)  # Open the file in the specified mode
    try:
        yield f  # Yield the file object to the context block
    finally:
        f.close()  # Ensure the file is closed after the block is executed


with open_file("demo.txt", "w") as f:  # Use the context manager to open a file
    f.write("This is a context manager example.\n")
