
with open("03-input") as f:
    str_lines = f.read().splitlines()

test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".splitlines()

def traverse(lines, dx, dy):
    x = y = trees = 0
    ymax = len(lines)
    xmax = len(lines[0])

    while y + dy < ymax:
        x = (x + dx) % xmax
        y += dy
        if lines[y][x] == "#":
            trees += 1

    return trees

one = lambda l: traverse(l, 3, 1)
assert one(test_data) == 7


def two(lines):
    return prod([
        traverse(lines, 1, 1),
        traverse(lines, 3, 1),
        traverse(lines, 5, 1),
        traverse(lines, 7, 1),
        traverse(lines, 1, 2)])

