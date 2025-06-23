# iterator version
class MyIterator:
    def __init__(self, limit):
        self.n = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration

# generator version
def my_generator(limit):
    for n in range(limit):
        yield n ** 2


print("Iterator version:", (list(MyIterator(10))))
print("Generator version:", [x for x in my_generator(10)])
