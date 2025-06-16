def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


info(name="Sam", age=30, city="Chennai")
