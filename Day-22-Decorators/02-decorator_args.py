def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for x in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(5)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
