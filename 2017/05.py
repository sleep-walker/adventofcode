def process(l, mode):
    # instruction pointer
    ip = 0
    # number of steps
    s = 0
    # until we jump out of the program
    while ip >= 0 and ip < len(l):
        s += 1                 # count the steps
        old = ip               # remember previous position
        ip += l[old]           # calculate the jump
        if mode == 2:          # if this is 2. part of the task
            if ip - old >= 3:  #  decrease long jump on position
                l[old] -= 1
            else:
                l[old] += 1    #  and increase otherwise
        else:
            l[old] += 1        # in 1. part we just increment

    return s

# read the file
with open("05-input", "r") as f:
    l = f.read().splitlines()

# convert program to integers
l = [int(x) for x in l]

demo = [0, 3, 0, 1, -3]
