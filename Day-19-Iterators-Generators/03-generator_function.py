def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(10):
    print(i)
