class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 100:
            raise StopIteration
        self.current += 1
        return self.current


for num in CountDown(0):
    print(num)
