import re

re_instruction = re.compile("^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

with open("06-input") as f:
    contents = f.read().splitlines()

class Lights:
    _grid = [[0 for j in range(1000)] for i in range(1000)]

    def part1_mode(self, mode, x, y):
        if mode == "turn on":
            self._grid[x][y] = 1
        elif mode == "turn off":
            self._grid[x][y] = 0
        elif mode == "toggle":
            self._grid[x][y] ^= 1

    def part2_mode(self, mode, x, y):
        if mode == "turn on":
            self._grid[x][y] += 1
        elif mode == "turn off":
            self._grid[x][y] -= 1 if self._grid[x][y] else 0
        elif mode == "toggle":
            self._grid[x][y] += 2

    def process_instruction(self, instruction, part_mode):
        m = re_instruction.match(instruction)
        result = m.groups()
        mode = result[0]
        x1, y1, x2, y2 = [int(i) for i in result[1:]]

        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                getattr(self, part_mode)(mode, x, y)

    def count_lighten_up(self):
        return sum((1 for y in self._grid for v in y if v))

    def sum_brightness(self):
        return sum((v for y in self._grid for v in y))

def part_1(contents):
    l = Lights()
    for i in contents:
        l.process_instruction(i, "part1_mode")
    return l.count_lighten_up()

def part_2(contents):
    l = Lights()
    for i in contents:
        l.process_instruction(i, "part2_mode")
    return l.sum_brightness()
