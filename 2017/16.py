import copy

init_p = "".join([chr(ord('a') + i) for i in range(16)])
p = init_p
def spin(n, l):
    n = int(n)
#    print ("spin: %s" % n)
    return l[-n:] + l[:-n]

def xchange(i, j, l):
    i, j = int(i), int(j)
#    print ("xchange: %s <--> %s" % (i, j))
    l = [x for x in l]
    x = l[i]
    l[i] = l[j]
    l[j] = x
    return "".join(l)

def partner(a, b, l):
#    print ("partner: %s <--> %s" % (a, b))
    return l.replace(a, '~').replace(b, a).replace('~', b)


with open("16-input", "r") as f:
    inp = f.read().splitlines()[0].split(",")

def dance():
    global p
    for l in inp:
        if l[0] == 's':
            p = spin(l[1:], p)
        elif l[0] == 'x':
            i, j = l[1:].split('/')
            p = xchange(i, j, p)
        elif l[0] == 'p':
            a, b = l[1:].split('/')
            p = partner(a, b, p)
#        print p

# one cycle
#print p

def perm():
    global p
    # permutation created from result
    np = [
        p[6], p[8], p[0], p[3], p[7], p[12], p[10], p[15], p[2], p[13], p[1], p[5], p[9], p[4], p[11], p[14]]
    #(6,8,0,3,7,12,10,15,2,13,1,5,9,4,11,14)
    #(0,6,10,1,8,2)(3)(4,7,15,14,11,5,12,9,13)
    p = np
#print p

def find_period():
    dance()
    i = 1
    while p != init_p:
        dance()
        i += 1
    return i

def cycles(n):
    global init_p, p
#    init_p = [x for x in init_p]
    p = copy.copy(init_p)
    for i in range(n):
#        perm()
        dance()
    return p

def s_cycles(n):
    period = find_period()
    return cycles(n % period)

print s_cycles(1000000000)
