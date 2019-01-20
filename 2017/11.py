dsc = """
original:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

sw  /\ nw
   /  \
  |    |
s |    | n
  |    |
   \  /
se  \/ ne
"""


class HexGrid(object):
    def __init__(self):
        self.pos = (0, 0)
        self.max = 0

    def walk(self, d):
        if d == "n":
            dx, dy = (1, 0)
        elif d == "s":
            dx, dy = (-1, 0)
        elif d == "ne":
            dx, dy = (1, -1)
        elif d == "nw":
            dx, dy = (0, 1)
        elif d == "se":
            dx, dy = (0, -1)
        elif d == "sw":
            dx, dy = (-1, 1)
        else:
            raise Exception("Unexpected direction")

        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.max = max(self.max, self.distance())

    def distance(self):
        x, y = self.pos
        # walk to x == 0 first
        # for each y we eat two x
        # x = 
        # dist = 2 * y + x % 2 + x - y
        # dist = y
        x = abs(x)
        y = abs(y)
        dist = x + (max(0,y - x/2 - x % 2))
        dist = max(abs(y), abs(x), abs(x - y))
        return dist


def find_child(directions):
    dirs = directions.split(",")
    hg = HexGrid()
    for d in dirs:
        hg.walk(d)
    print hg.pos
    return hg

with open("11-input", "r") as f:
    inp = f.read().splitlines()[0]

hg = find_child(inp)
