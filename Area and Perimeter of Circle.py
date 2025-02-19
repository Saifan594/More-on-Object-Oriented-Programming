print("\033c")

import math

class Circle():
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter the radius of the circle: "))

circle = Circle(r)

a = circle.area()
p = circle.perimeter()

print(f"Area of the circle: {a}")
print(f"Perimeter of the circle: {p}")