from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area =", self.l * self.b)

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area =", 3.14 * self.r * self.r)

r = Rectangle(5, 4)
r.area()

c = Circle(3)
c.area()