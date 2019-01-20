AQ = 16807
BQ = 48271

bits = (1 << 16) - 1

def print_bin(n):
    s = "{0:b}".format(n).zfill(32)
    print s[:16] + " " + s[16:]

def next_a(a, part2=False):
    a = (a*AQ) % 2147483647
    while part2 and (a % 4 != 0):
        a = (a*AQ) % 2147483647
    return a

def next_b(b, part2=False):
    b = (b*BQ) % 2147483647
    while part2 and (b % 8 != 0):
        b = (b*BQ) % 2147483647
    return b

def all(init_a, init_b, cycles=40000000, visual=False, part2=False):
    match = 0
    a = init_a
    b = init_b

    for i in range(cycles):
        a = next_a(a, part2)
        b = next_b(b, part2)
        if visual:
            print_bin(a)
            print_bin(b)
            print ""
        match += int((a & bits) == (b & bits))

    return match

#all(65, 8921)
print "part1: %s" % all(277, 349)
print "part2: %s" % all(277, 349, cycles=5000000, part2=True)
