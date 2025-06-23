class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"


b = Book("Harry Potter-The Philosopher's Stone")
print(b)
