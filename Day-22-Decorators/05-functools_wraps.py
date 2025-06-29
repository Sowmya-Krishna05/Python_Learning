from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@decorator
def greet(name):
    """Greet a person by name."""
    return f"Hi {name}!"


print("greet.__name__ :", greet.__name__)
print("greet.__doc__ :", greet.__doc__)

greet("Alice")
