with open("08-input") as f:
    contents = f.read().splitlines()

def part1(contents):
    return sum(len(line) - len(eval(line)) for line in contents)

assert part1([
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"']) == 12

def encode(x):
    result = x
    result = result.replace('\\', '\\\\')
    result = result.replace('"', '\\"')
    result = f'"{result}"'
    return result

assert encode(r'""') == r'"\"\""'
assert encode(r'"abc"') == r'"\"abc\""'
assert encode(r'"aaa\"aaa"') == r'"\"aaa\\\"aaa\""'
assert encode(r'"\x27"') == r'"\"\\x27\""'

def part2(contents):
    return sum(len(encode(line)) - len(line) for line in contents)

assert part2([r'""',
              r'"abc"',
              r'"aaa\"aaa"',
              r'"\x27"']) == 19
