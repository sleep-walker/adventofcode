#!/usr/bin/env python3


with open("/home/tcech/Stažené/adventofcode/3-input", "r") as f:
    lines = f.read().splitlines()

class Square(object):
    nid = ''
    posx = -1
    posy = -1
    sizex = -1
    sizey = -1

    def __init__(self, str):
        self.parse_string(str)

    def parse_string(self, str):
        self.nid,  str  = str.split(" @ ", 1)
        posx, str  = str.split(",", 1)
        posy, str  = str.split(": ", 1)
        sizex, sizey = str.strip().split("x", 1)
        self.posx = int(posx)
        self.posy = int(posy)
        self.sizex = int(sizex)
        self.sizey = int(sizey)


class Fabric(object):
    content = [[0 for i in range(1000)] for j in range(1000)]

    def add_square(self, x, y, sx, sy):
        for i in range(x, x+sx):
            for j in range(y, y+sy):
                self.content[i][j] += 1

    # first
    def square_overlap(self):
        return sum([1 for row in self.content for col in row if col > 1])

    def check_square(self, x, y, sx, sy):
        alone = True
        for i in range(x, x+sx):
            for j in range(y, y+sy):
                if self.content[i][j] != 1:
                    alone = False
                    break
        return alone

f = Fabric()
squares = []
for i in lines:
    squares.append(Square(i))

for s in squares:
    f.add_square(s.posx, s.posy, s.sizex, s.sizey)

for s in squares:
    if f.check_square(s.posx, s.posy, s.sizex, s.sizey):
        print("ID: %s" % s.nid)
        break

