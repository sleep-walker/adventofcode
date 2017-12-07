def row_cksum(row):
    r = row.split("\t")
    min = int(r[0])
    max = int(r[0])
    for i, n in enumerate(r):
        n = int(n)
        if n < min:
#            print "%s < %s" % (n, min)
            min = n
        if n > max:
#            print "%s > %s" % (n, max)
            max = n
    return max - min

def row_cksum2(row):
    r = row.split("\t")
    for i, m in enumerate(r):
        m = int(m)
        for j, n in enumerate(r):
            n = int(n)
            if j <= i:
                continue
            if (m % n == 0):
                print "%s / %s = %s (zb. %s)" % (m, n, m/n, m%n)
                return m / n
            if (n % m == 0):
                print "%s / %s = %s (zb. %s)" % (n, m, n/m, n%m)                
                return n / m
    raise Exception("number not found")

def cklines(inp):
    s = 0
    for l in inp.splitlines():
#        s += row_cksum(l)
        s += row_cksum2(l)
    return s

