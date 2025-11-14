# line_eq.py
# TODO #1: Método __eq__ para comparar líneas con puntos equivalentes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return (
            isinstance(other, Line) and
            ((self.p1 == other.p1 and self.p2 == other.p2) or
             (self.p1 == other.p2 and self.p2 == other.p1))
        )

# Ejemplo de prueba

if __name__ == "__main__":
    a = Point(1, 2)
    b = Point(3, 4)
    l1 = Line(a, b)
    l2 = Line(Point(3, 4), Point(1, 2))
    print("¿Las líneas son equivalentes?", l1 == l2)  # True


# line_midpoint.py
# TODO #2: Método midpoint para la clase Line

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        mx = (self.p1.x + self.p2.x) / 2
        my = (self.p1.y + self.p2.y) / 2
        return Point(mx, my)

# Ejemplo de prueba
if __name__ == "__main__":
    l = Line(Point(0,  0), Point(4, 4))
    mid = l.midpoint()
    print("Punto medio:", mid)  # Point(2.0, 2.0)


# rectangle_midpoint.py
# TODO #3: Método midpoint para la clase Rectangle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def midpoint(self):
        mx = (self.lower_left.x + self.upper_right.x) / 2
        my = (self.lower_left.y + self.upper_right.y) / 2
        return Point(mx, my)

# Ejemplo de prueba
if __name__ == "__main__":
    r = Rectangle(Point(0, 0), Point(4, 6))
    center = r.midpoint()
    print("Centro del rectángulo:", center)  # Point(2.0, 3.0)






