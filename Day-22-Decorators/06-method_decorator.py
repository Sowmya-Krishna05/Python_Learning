def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper


class Greeter:
    @log_method
    def greet(self, name):
        print(f"Hello, {name}!")


Greeter().greet("Alice")
