print("\033c")

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def rectangleArea(self):
        return self.length * self.width

newRactangle = Rectangle(12, 10)

result = newRactangle.rectangleArea()

print(f"The area of Rectangle: {result}")