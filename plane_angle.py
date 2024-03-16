import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Point(self.y * other.z - self.z * other.y,
                     self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.x)

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    

def plane_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C

    X = AB.cross(BC)
    Y = BC.cross(CD)

    cos_F = X * Y / (X.magnitude() * Y.magnitude())
    F = math.degrees(math.acos(cos_F))

    return F

A = Point(0, 0, 0)
B = Point(1, 0, 0)
C = Point(0, 1, 0)
D = Point(0, 0, 1)

angle = plane_angle(A, B, C, D)
print(f"Угол между плоскостями: {angle} градусов")