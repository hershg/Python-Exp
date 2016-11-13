class Car:
    def __init__(self, color):  # special method __init__ for initializing parameters
        self.color = color      # __init__ always takes "self" as parameter (reference to object being created)



car = Car("blue")  # Note: don't pass self parameter explicitly, only other parameters

print(car.color)





# "self" is passed for function definitions in classes; refers to object being created
class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current



