#!/usr/bin/env python3

import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("six")


SIZE_X = 1750
SIZE_Y = 1750

SHIFT = 450

with open("/home/tcech/Stažené/adventofcode/6-input", "r") as f:
    lines = f.read().splitlines()

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

coords = []

for i in lines:
    x = i.split(", ")
    coords += [(int(x[0]), int(x[1]))]


def shift_coords(coords, shiftx, shifty):
    return [ (x + shiftx, y + shifty) for x, y in coords]


def create_field(sizex, sizey, coords, shiftx, shifty):
    field = [[0 for i in range(sizex)] for j in range(sizey)]

    sc = shift_coords(coords, shiftx, shifty)
    for y in range(sizey):
        for x in range(sizex):
            m = 10000
            for c in range(len(sc)):
                d = distance(sc[c], (x, y)) 
                if d < m:
                    m = d
                    field[x][y] = c
                elif d == m:
                    field[x][y] = -1


    bound_minx = min([x for x, y in sc])
    bound_maxx = max([x for x, y in sc])
    bound_miny = min([y for x, y in sc])
    bound_maxy = max([y for x, y in sc])

    # make data flat
    data = Counter([y for x in field for y in x])

    # sort by number of occurences
    com = data.most_common()

    return com


def one():
    com1 = create_field(1500, 1500, coords, 230, 270)
    com2 = create_field(800, 800, coords, 200, 200)

    intersection = set(com1).intersection(set(com2))
    print(intersection[0][1])

def create_field2(sizex, sizey, coords, shiftx, shifty):
    # field = [[0 for i in range(sizex)] for j in range(sizey)]

    sc = shift_coords(coords, shiftx, shifty)
    # for y in range(sizey):
    #     for x in range(sizex):
    #         field[x][y] = sum(distance(c, (x, y)) for c in sc)

    return [[sum(distance(c, (x, y)) for c in sc) for x in range(sizex)] for y in range(sizey)]

def filter_threshold(field, t):
    region = [y for x in field for y in x if y < t]
    return len(region)

def two():
    field = create_field2(2000, 2000, coords, 700, 700)
    print ("two: %d" % filter_threshold(field, 10000))





#field = [[min([distance((i, j), c) for c in coords]) for i in range(350)] for j in range(350)]

# max_coords = (-1, -1)
# maximum = 0
# for y in range(350):
#     for x in range(350):
#         if field[x][y] > maximum:
#             max_coords = (x, y)
#             maximum = field[x][y]
