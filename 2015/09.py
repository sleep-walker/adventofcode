from operator import itemgetter
import itertools

with open("09-input") as f:
    contents = f.read().splitlines()


class Map():
    table = {}
    def __init__(self, contents):
        for line in contents:
            cities, distance = line.split(" = ", 1)
            origin, target = cities.split(" to ", 1)
            self.table.setdefault(origin, {})[target] = int(distance)
            self.table.setdefault(target, {})[origin] = int(distance)

    def distance(self, p):
        d = 0
        last = p[0]
        for c in p[1:]:
            d += self.table[last][c]
            last = c
        return d

    def generate_routes(self):
        return ((self.distance(permutation), permutation) for permutation in itertools.permutations(self.table))

# I can be stupid here 8 cities gives 40320 permutations
def part1(contents):
    m = Map(contents)
    return min(m.generate_routes(), key=itemgetter(0))[0]

assert part1([
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"]) == 605

def part2(contents):
    m = Map(contents)
    return max(m.generate_routes(), key=itemgetter(0))[0]

assert part2([
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"]) == 982
