import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def describe(self):
        print(f"This is a shape with x {self.x} and y {self.y}")

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y = other.y
        return math.hypot(dx, dy)

    def __str__(self):
        return f"<Shape: {self.x=} {self.y=}"


if __name__ == "__main__":
    s = Shape(1,2)
    print(s)
    s.describe()

    p = Shape(10, 20)
    print(s.distance(p))
