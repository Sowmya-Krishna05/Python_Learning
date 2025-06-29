class fileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
# The __init__ method is the class constructor.
# It takes two arguments: file_name (the name of the file to open) and mode (the mode in which to open the file)

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.file_name, self.mode) # Open the file and assign it to self.file
        return self.file # The __enter__ method is called when entering the context.

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close() # The __exit__ method is called when exiting the context.


with fileManager("custom.txt", "w") as f:
    f.write("Custom context manager example.\n")
