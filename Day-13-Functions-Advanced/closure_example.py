def outer(x):
    def inner(y):
        return x * y
    return inner


add = outer(5)
print(add(3))
