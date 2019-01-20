def lpos(time, depth, shift=0):
    #t = 10
    # depth = 5
    # 0,1,2,3,4
    # 0,1,2,3,4,3,2,1
    # 0 --> . --> 0
    if depth == 0:
        # never bothers
        return 1
    # 1 --> 0 --> 0
    # 2 --> 0,1 --> 2
    # 3 --> 0,1,2,1 --> 4
    # 4 --> 0,1,2,3,2,1 --> 6
    steps = 2 * depth - 2

    # period of repeat is count of 'steps'
    time = (time + shift) % steps
    if time < depth:
        res = time
        return res
    if time < steps:
        res = (steps - time)
        return res
    return -27

def lpos_iscaught(time, shift=0):
    return lpos(time, fw[time], shift) == 0
fw = [0 for i in range(89)]
def create_firewall(inp):
    for l in inp.splitlines():
        s, ls = [int(x) for x in l.split(":")]
#        fw[s] = (0, 1, ls)
        fw[s] = ls

def calc_severity(pos):
    return pos * fw[pos]

test_inp = """0: 3
1: 2
4: 4
6: 4
"""

with open("13-input", "r") as f:
    inp = f.read()

#create_firewall(test_inp)

create_firewall(inp)

print "part 1 sum is: %s" % sum([x * fw[x] for x in range(len(fw)) if lpos_iscaught(x, 0)])

def find_delay():
    i = 0
    while True:
        # if i % 1000 == 0:
        #     print i
        if [x * fw[x] for x in range(len(fw)) if lpos_iscaught(x, i)] == []:
            return i

        i += 1

print "part 2 delay is: %s" % find_delay()
