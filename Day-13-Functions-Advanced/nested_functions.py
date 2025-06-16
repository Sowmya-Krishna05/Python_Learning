def outer():
    def inner():
        print("Inner function")

    inner()


outer()
