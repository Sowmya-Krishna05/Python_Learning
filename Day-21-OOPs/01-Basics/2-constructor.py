class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


my_car = Car("Hyundai", "black")
print(type(my_car))
print(my_car.brand)
print(my_car.color)
