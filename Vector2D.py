import math


class vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alpha = 0
        self.distance = 0
        self.calcpolar = False
        self.length = -1
        self.normx = -10
        self.normy = -10

    def __add__(a, b):
        return vec2(a.x + b.x, a.y + b.y)

    def __sub__(a, b):
        return vec2(a.x - b.x, a.y - b.y)

    def __str__(self):
        return "Vector2 x:" + str(self.x) + " y:" + str(self.y)

    def topolar():
        self.calcpolar = True
        self.atan(self.y / self.x)
        self.distance = math.sqrt(self.x ** 2 + self.y ** 2)
        return (self.alpha, slef.distance)

    def __truediv__(a, b):
        return vec2(a.x / b.x, a.y / b.y)

    def __rmul__(a, b):
        if type(b) == type(1.0):
            return vec2(a.x * b, a.y * b)

        if type(a) == type(1.0):
            return vec2(b.x * a, b.y * a)

        return vec2(a.x * b.x, a.y * b.y)

    def __eq__(b):
        if (b.x == self.x) and (b.y == self.y):
            return true
        else:
            return false

    def norm(self):
        if self.normx == -10:
            if self.l == -1:
                self.length()
            self.normx = self.x / self.l
            self.normy = self.y / self.l

    def length(self):
        if self.l == -1:
            self.l = math.sqrt(self.x ** 2 + self.y ** 2)

        return self.l

    def distance(self, b):
        return (self - b)


nullvec = vec2(0, 0)       