import math
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
R1 = Rectangle(8, 10)
C1 = Circle(7)
lst = [R1, C1]
for i in lst:
    print(i.area())