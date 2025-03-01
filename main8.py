import math

class Circle:
    def __init__(self, radius):
        # Constructor to initialize the radius
        self.radius = radius

    def area(self):
        # Method to compute the area of the circle
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Method to compute the perimeter (circumference) of the circle
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)  # Create a circle with radius 5

# Compute and print the area and perimeter
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")
