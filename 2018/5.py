#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("five")
#log.setLevel(logging.DEBUG)

with open("/home/tcech/Stažené/adventofcode/5-input", "r") as f:
    lines = f.read().splitlines()

def remove_two(s, pos):
    log.debug("removing: %s @%d", s, pos)
    if pos > len(s) - 2:
        raise Exception("Wrong slicing: %s, @%d" % (s, pos))
    return s[:pos] + s[pos+2:]

def reduce_polymer(s):
    log.debug("len: %d", len(s))
    l = len(s) + 1
    changed = True
    i = 0
    while changed:
        changed = False
        while i < len(s) - 1:
            log.debug("i: %d", i)
            reverse_case = (s[i].islower() != s[i+1].islower())
            same_letter = (s[i].lower() == s[i+1].lower())
            if reverse_case and same_letter:
                # cut it out
                s = s[:i] + s[i+2:] #remove_two(s, i)
                changed = True
                i -= 1
                if i < 0:
                    i = 0
                break
            else:
                i += 1
    return s

assert(reduce_polymer("dabAcCaCBAcCcaDA") == "dabCBAcaDA")

inp = lines[0]
x = reduce_polymer(inp)
# part one
print("Length: %d" % len(x))

# part two
elements = set(inp.lower())
m = 50002
for e in elements:
    low_e = e.lower()
    up_e = e.upper()
    stripped = "".join([i for i in inp if i != low_e and i != up_e])
    r = reduce_polymer(stripped)
    m = min(m, len(r))

print("Minimum: %d" % m)
