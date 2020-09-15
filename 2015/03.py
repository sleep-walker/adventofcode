with open("03-input") as f:
    contents = f.read()

moves = {
    '^': ( 0, -1),
    'v': ( 0,  1),
    '<': (-1,  0),
    '>': ( 1,  0)
}

def move(original, c):
    return original[0] + moves[c][0], original[1] + moves[c][1]

def part_1(contents):
    santa = (0, 0)
    visited = set([santa])
    for s in contents:
        santa = move(santa, s)
        visited.add(santa)
    return len(visited)

assert part_1('^v') == 2
assert part_1('^>v<') == 4
assert part_1('^v^v^v^v^v') == 2

def part_2(contents):
    santa = (0,0)
    robo = (0,0)
    visited = set([santa])
    for s, r in zip(contents[0::2], contents[1::2]):
        santa = move(santa, s)
        robo = move(robo, r)
        visited.add(santa)
        visited.add(robo)
    return len(visited)

assert part_2('^v') == 3
assert part_2('^>v<') == 3
assert part_2('^v^v^v^v^v') == 11
