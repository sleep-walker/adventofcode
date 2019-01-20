buffer = []
pos = 0
def init():
    global buffer, pos
    buffer = [0]
    pos = 0

def insert(step, val):
    global pos, buffer
    pos = (pos + step) % len(buffer) + 1
    buffer.insert(pos, val)

def process(step=3, rmax=2018):
    for i in range(1, rmax):
        insert(step, i)

def printout():
    print " ".join([str(i) for i in buffer[:pos]]) + " (" + str(buffer[pos]) + ") " + " ".join([str(i) for i in buffer[pos+1:]])
init()

def part1():
    process(303)
    i = buffer.index(2017)
    print buffer[i+1]

def part2():
    process(303, 50000000)
    i = buffer.index(0)
    print buffer[i+1]

# let's track only position
def len_after_n(n):
    return n + 1

# position of last number
def position_after_n(n, step=303):
    pos = 0
    for i in range(1,n):
        pos = (pos + step) % n
    return pos


