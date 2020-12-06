def once(start):
    out = ""
    last = None
    count = 1
    for c in start:
        if c == last:
            count += 1
        else:
            if last:
                out += f"{count}{last}"
            last = c
            count = 1
    if last is not None:
        out += f"{count}{last}"
    return out

assert once("1") == "11"
assert once("11") == "21"
assert once("21") == "1211"
assert once("1211") == "111221"
assert once("111221") == "312211"

def part1(start):
    x = start
    for i in range(40):
        x = once(x)
    return len(x)

def part2(start):
    x = start
    for i in range(50):
        x = once(x)
    return len(x)
