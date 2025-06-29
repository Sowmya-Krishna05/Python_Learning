class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before call")
        result = self.func(*args, **kwargs)
        print("After call")
        return result


@DecoratorClass
def say_hello():
    print("Hello!")


say_hello()
