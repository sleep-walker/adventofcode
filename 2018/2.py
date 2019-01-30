#!/usr/bin/env python3

def count_letters(word):
    doubles = 0
    thrices = 0
    s = sorted(word)
    st = set(s)
    for i in st:
        c = s.count(i)
        if c == 3:
            thrices = 1
        if c == 2:
            doubles = 1
    return (doubles, thrices)

with open("/home/tcech/Stažené/adventofcode/2-input", "r") as f:
    lines = f.read().splitlines()

d = 0
t = 0

# first part
for l in lines:
    nd, nt = count_letters(l)
    d += nd
    t += nt

# second part
slines = sorted([sorted(l) for l in lines])

count = len(lines)

for i in range(next(iter(set([len(s) for s in lines])))):
    slines = [r[:i] + r[i+1:] for r in lines]
    sslines=set(slines)
    c = len(sslines)
    if c != count:
        for j in sslines:
            if slines.count(j) > 1:
                print(j)

