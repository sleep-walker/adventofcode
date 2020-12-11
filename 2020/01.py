from itertools import combinations
from math import prod
from functools import partial

with open("01-input") as f:
    str_lines = f.read().splitlines()

lines = [int(l) for l in str_lines]
test_input = [1721, 979, 366, 299, 675, 1456]

def n_tuples(n, l):
    for c in combinations(l, n):
        if sum(c) == 2020:
            return prod(c)

one = partial(n_tuples, 2)
two = partial(n_tuples, 3)

assert one(test_input) == 514579
assert two(test_input) == 241861950
