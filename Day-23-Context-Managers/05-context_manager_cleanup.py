class SafeOpen:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Opening file safely...")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An error occurred: {exc_value}")
        print("Closing file safely...")
        self.file.close()
        return True


with SafeOpen("practice.txt") as f:
    f.write("Trying something risky")
    raise ValueError("Simulated Error!")
