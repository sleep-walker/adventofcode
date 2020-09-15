from functools import reduce

with open("02-input") as f:
    contents = f.read().splitlines()

def paper(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    sizes = [x*y, x*z, y*z]
    return 2*sum(sizes) + min(sizes)

def ribbon(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    sizes = [x, y, z]
    return 2 * sum(sizes) - 2 * max(sizes) + reduce(lambda x, y: x*y, sizes)

def process(contents, fn):
    sum = 0
    for line in contents:
        sum += fn(*line.split("x"))
    return sum

def part_1(contents):
    return process(contents, paper)

assert part_1(['2x3x4']) == 58
assert part_1(['1x1x10']) == 43

def part_2(contents):
    return process(contents, ribbon)

assert part_2(['2x3x4']) == 34
assert part_2(['1x1x10']) == 14
