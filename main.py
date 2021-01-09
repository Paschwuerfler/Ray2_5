
"""
TODO:
-Input handling
-Coluring should be done in relitve terms to enale colour support

"""


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mymath import *
from Canvas import canvas
from Player import player
from Vector2D import vec2
from Vector2D import nullvec
from Line2D import line
import time

m = canvas(40,20)


def render():
    m.clear()
    vv = 0
    for a in range(ply.ang, ply.ang+180, 5):
        vv += 1
        sigv = line(ply.pos, ply.pos + vec2(sind(a), cosd(a)), shades[1])
        for o in env:
            res = sigv.hit(o)
            #print(type(res))
            if 0 < res[1] < 1 and res[0] > 0:
                #print(res[0])
                m.draw(vv,1/res[0], o.col)


if __name__ == '__main__':
# i will probably put some of this code in an "Environment" class someday
    #this is for very simple testing
    #collsision detction can be ralised with the vector classes also.

    #create a simpüle test environment
    #points
    shades = ["░", "▒", "▓", "█"]

    a = vec2(0, 0)
    b = vec2(2, 0)
    c = vec2(2, 2)
    d = vec2(0, 2)
    env = [line(a,b,shades[2]), line(b,c,shades[2]), line(c,d,shades[3]), line(d,a,shades[3])]

    ply = player(vec2(1, 1),0)



    for i in range(0,360,10):
        ply.ang = i
        render()
        m.output()
        print("--")
        time.sleep(0.1)
        



