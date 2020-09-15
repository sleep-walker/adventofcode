
with open("01-input") as f:
    contents = f.read()

def part_1(contents):
    return sum((1 for i in contents if i == '(')) - sum((1 for i in contents if i == ')'))

assert part_1('(())') == 0
assert part_1('()()') == 0

assert part_1('(((') == 3
assert part_1('(()(()(') == 3
assert part_1('))(((((') == 3

assert part_1('())') == -1
assert part_1('))(') == -1

assert part_1(')))') == -3
assert part_1(')())())') == -3


def part_2(contents):
    floor = 0
    for i, c in enumerate(contents):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            return i + 1
    return None

assert part_2(')') == 1
assert part_2('()())') == 5
