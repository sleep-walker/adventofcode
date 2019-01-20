import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# log.setLevel(logging.WARN)

class CircularList(list):
    def __getitem__(self, i):
        return super(CircularList, self).__getitem__(i % len(self))
    def __setitem__(self, i, val):
        return super(CircularList, self).__setitem__(i % len(self), val)

    # slow but simple
    def __getslice__(self, i, j):
        # log.debug("getslice %s, %s", i, j)
        sl = []
        for idx in range(i, j):
            sl.append(self[idx])
        return sl

    # def __setslice__(self, i, j, y):
    #     y.reverse()
    #     for idx in range(i, j):
    #         self[idx] = y.pop()
    #     return self


def in_place_reverse(inp, start, length):
#    log.debug("inp before: %s", inp)
    for i in range(0, length / 2):
        a = start + i
        b = start + length - 1 - i
 #       log.debug("a = %s, b = %s", a, b)
 #       log.debug("inp[a] = %s, inp[b] = %s", inp[a], inp[b])
        x = inp[a]
        inp[a] = inp[b]
        inp[b] = x
#    log.debug("inp after: %s", inp)
    return inp
    #     in
    # before = inp[0:start]
    # after = inp[(start + length):len(inp)]
    # process = inp[start:length]
    # process.reverse()
    # print
    # return before + process + after


def process(inp, lengths):
    skip = 0
    pos = 0
    for l in lengths:
#        log.debug("inp: %s", inp)
#        log.debug("pos = %s, skip = %s, l = %s", pos, skip, l)
        inp = in_place_reverse(inp, pos, l)
        pos = (pos + skip + l) % len(inp)
        skip += 1

    return inp

def densify_hash(sparse_hash):
    dense_hash = []
    for i in range(16):
        x = 0
        for j in sparse_hash[i*16:(i+1)*16]:
            x = x ^ j
        dense_hash.append(x)
    return dense_hash

def hexstring(h):
    return "".join( "%02x" % x for x in h)

def str2inp(s):
    return [ord(x) for x in s]

suffix = [17, 31, 73, 47, 23]
def str2inpwithsuffix(s):
    return str2inp(s) + suffix


def get_dense(s):
    inp = str2inpwithsuffix(s)
    sparse_hash = process(CircularList(range(256)), 64*inp)
    dense_hash = densify_hash(sparse_hash)
    print hexstring(dense_hash)
    return dense_hash
# test
#inp = process(CircularList(range(5)), [3, 4, 1, 5])

# part1
lengths = [206, 63, 255, 131, 65, 80, 238, 157, 254, 24, 133, 2, 16, 0, 1, 3]
inp = process(CircularList(range(256)), lengths)
print "part 1: %s" % (inp[0] * inp[1])

lengths_ascii = ",".join(str(x) for x in lengths)

print "part 2: ",
get_dense(lengths_ascii)

