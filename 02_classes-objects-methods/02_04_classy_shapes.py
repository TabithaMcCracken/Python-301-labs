# Done
# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle():
    """Models a rectangle"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter

    def rectangle_area(self):
        area = self.length * self.width
        return area

    def __str__(self):
        return f"Rectangle length and width: ({self.length}, {self.width})" 

    def __repr__(self):
        return f"Rectangle (length={self.length}, width={self.width})"

rectangle1 = Rectangle(4, 5)
print(f"The perimeter of the rectangle is : {rectangle1.rectangle_perimeter()}")
print(f"The area of the rectangle is: {rectangle1.rectangle_area()}")

class Circle():
    """Models a circle"""

    def __init__(self, radius):
        self.radius = radius

    def circle_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def circle_area(self):
        area = 3.14 * (self.radius**2)
        return area  

    def __str__(self):
        return f"Circle Radius: ({self.radius})" 

    def __repr__(self):
        return f"Circle (radius={self.radius})"

circle1 = Circle(5)
print(f"The perimeter of the circle is : {circle1.circle_perimeter()}")
print(f"The area of the circle is: {circle1.circle_area()}")