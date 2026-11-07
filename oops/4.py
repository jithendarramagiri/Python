class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

side = float(input("Enter side of square: "))
square = Square(side)
print(f"Area of Square: {square.area()}")
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle = Triangle(base,height)
print(f"Area of Triangle: {triangle.area()}")
