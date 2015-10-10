class Vector2D:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


v1 = Vector2D()
v2 = Vector2D(1, 1)
v3 = Vector2D(1, 5)

v1 = v2 + v3
print v1


