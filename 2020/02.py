import re
from functools import partial

with open("02-input") as f:
    str_lines = f.read().splitlines()


line_re = re.compile("^([0-9]+)-([0-9]+) (.): (.*)$")

def valid_password_one(l):
    m = line_re.match(l)
    mi = int(m.group(1))
    mx = int(m.group(2))
    ch = m.group(3)
    password = m.group(4)
    return password.count(ch) in range(mi, mx + 1)

def valid_password_two(l):
    m = line_re.match(l)
    p1 = int(m.group(1)) - 1
    p2 = int(m.group(2)) - 1
    ch = m.group(3)
    password = m.group(4)
    return (password[p1] + password[p2]).count(ch) == 1

def check(fn, lines):
    results = [1 for l in lines if fn(l)]
    return len(results)


one = partial(check, valid_password_one)
two = partial(check, valid_password_two)

assert one(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2
assert two(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 1
