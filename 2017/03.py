DIR=[(1, 0), (0, 1), (-1, 0), (0, -1)]

# sum of all the numbers around
def field_sum(a, x, y):
    s = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            # don't count x,y to sum
            if dx == 0 and dy == 0:
                continue
            if (x+dx, y+dy) in a:
                s += a[(x+dx, y+dy)]
    return s

def create_field(n):
    i = 1               # starting number
    d = 0               # starting direction
    x = 0               # starting position
    y = 0               # starting position
    a = {(0, 0): 1}     # initialization of the field
    nd = 1              # next direction
    while i < n:
        # if we can change direction to next one
        if (x + DIR[nd][0], y + DIR[nd][1]) not in a:
            # do it
            d = nd
            nd = (d + 1) % 4
        # apply difference
        x += DIR[d][0]
        y += DIR[d][1]
        i += 1
        a[(x,y)] = i

    return a, (x,y)

def create_field2(n):
    i = 1
    d = 0
    x = 0
    y = 0
    a = {(0, 0): 1}
    nd = 1
    while i <= n:
        if (x + DIR[nd][0], y + DIR[nd][1]) not in a:
            d = nd
            nd = (d + 1) % 4
        x += DIR[d][0]
        y += DIR[d][1]
        # we are not just incrementing, we're summing on position
        i = field_sum(a, x, y)
        a[(x,y)] = i

    return i, a

def dist(x, y):
    return abs(x) + abs(y)


def print_field(a):
    minx = min([x[0] for x in a.keys()])
    maxx = max([x[0] for x in a.keys()])
    miny = min([x[1] for x in a.keys()])
    maxy = max([x[1] for x in a.keys()])
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x,y) in a:
                print "%7d" % a[(x, y)],
            else:
                print "%7s" % "",
        print

