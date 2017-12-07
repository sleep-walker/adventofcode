# demo values
#inp = [0, 2, 7, 0]

# real values
with open("06-input", "r") as f:
    line = f.read().splitlines()[0]

inp = [int(x) for x in line.split("\t")]

linp = len(inp)
seen = {}

def cycle():
    global inp, seen
    # maximum value
    m = max(inp)

    # index of maximum value
    mi = inp.index(m)

    # remove the value
    inp[mi] = 0

    # and spread it to other banks
    while m > 0:
        # step to next bank, in the end go back to beginning
        mi = (mi + 1) % linp
        # increase the value in bank
        inp[mi] += 1
        # and decrease the pool of values
        m -= 1

#    print tuple(inp)

def debug():
    # initialize steps counter
    steps = 0

    while tuple(inp) not in seen:
        # remember the state we saw adn when we saw it
        seen.update({tuple(inp): steps})
        # do one balancing cycle
        cycle()
        # increment counter
        steps += 1
    # now we met state we've been before, we're in cycle...
    # ...and we remember when it was
    return steps, steps - seen[tuple(inp)]
