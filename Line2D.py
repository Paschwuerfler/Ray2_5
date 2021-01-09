class line():
    def __init__(self, a, b, col):
        self.posa = a
        self.posb = b
        self.dir = b - a
        self.col = col

    def hit(self, b):
        lam = 0
        mu = 0
        """
        if b.dir.norm() == self.dir.norm():
            return -1
        if self.dir == vec2(0,0) or b.dir == vec2(0,0):
            return -1
        """
        self.xa1 = self.posa.x
        self.ya1 = self.posa.y

        self.xd1 = self.dir.x
        self.yd1 = self.dir.y

        self.xa2 = b.posa.x
        self.ya2 = b.posa.y

        self.xd2 = b.dir.x
        self.yd2 = b.dir.y
        # x = (-c*h+a*h+d*(g- e))/(d*f-b*h)
        try:
            lam = (-self.xa2 * self.yd2 + self.xa1 * self.yd2 + self.xd2 * (self.ya2 - self.ya1)) / (
                        self.xd2 * self.yd1 - self.xd1 * self.yd2)
            # y = -(b*( e-g)+c*f-a*f)/(d*f-b*h)
            mu = -(self.xd1 * (self.ya1 - self.ya2) + self.xa2 * self.yd1 - self.xa1 * self.yd1) / (
                        self.xd2 * self.yd1 - self.xd1 * self.yd2)
        except:
            return 0, 0
        return lam, mu

        return lam, mu

    def distance(self, b):
        return (self.hit(b) - self.posa)

