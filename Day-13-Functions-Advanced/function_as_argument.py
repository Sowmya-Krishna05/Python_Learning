def apply(fn, value):
    return fn(value)


def double(x):
    return x ** 2


print(apply(double, 4))

# the apply function is called with double as the fn argument (a reference to the double function).
# 4 as the value argument.
# The apply function calls double(4), which computes 4 * 2 = 8.
