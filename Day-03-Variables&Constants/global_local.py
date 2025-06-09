x = "global"


def my_func():
    y = "local"
    print("Inside function, y =", y)


my_func()
print("Outside function, x =", x)
