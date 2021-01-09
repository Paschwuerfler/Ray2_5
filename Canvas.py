"""
TODO:
-A colour implementation would me nice, the question is weather or not i can implement this cross-
platform, there might be libraries to handle.


"""


class canvas():
    def __init__(self, x, y):
        self.sizex = x
        self.sizey = y
        self.m = []

        for i in range(x):
            self.m.append([])
            for o in range(y):
                self.m[i] += "░"

    def output(self):
        for i in range(self.sizey):
            s = ""
            for o in range(self.sizex):
                s += self.m[o][i]

            print(s)

    def clear(self):
        for i in range(self.sizex):
            for o in range(self.sizey):
                self.m[i][o] = "░"

    def draw(self, pos, size, col):
        # print("size"+ str(size))
        size *= 4

        # if (size/2) > self.sizey:
        #   size = self.sizey/2

        for i in range(int(size * 2)):
            self.m[pos][int(-i - self.sizey / 2)] = col
            # print(int(i+self.sizey/2))
            self.m[pos][int(i + self.sizey / 2)] = col