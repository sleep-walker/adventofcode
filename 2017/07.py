class Prg(object):
    def __init__(self, name, weight, subtowers):
        self.name = name
        self.weight = weight
        self.subtowers_s = subtowers
        self.subs = set()
        self.ontop_of = set()

    def __str__(self):
        s = "%s (%s)" % (self.name, self.weight)
        if self.subtowers_s:
            s += " --> %s" % ", ".join(x.name for x in self.subs)
        if hasattr(self, 'whole'):
            s += " [whole: %s]" % self.whole
        if hasattr(self, 'subweights'):
            s += " %s" % self.subweights
        return s

def read_line(line):
#    print ("reading: %s" % line)
    tokens = line.split(" ")
    name = tokens[0]
    weight = int(tokens[1][1:-1])
    if len(tokens) > 2:
        subtowers = [x[:-1] if x.endswith(",") else x for x in tokens[3:]]
    else:
        subtowers = []
    return Prg(name, weight, subtowers)

with open("07-input", "r") as f:
    lines = f.read().splitlines()

#programs = set()
programs = {}

# read the data
for l in lines:
    p = read_line(l)
    programs.update({p.name: p})

# now create real link for each program
for n, p in programs.iteritems():
#    p = programs[n]
    p.subs = set(programs[x] for x in p.subtowers_s)
#    print "created: %s" % p
    for x in p.subs:
        x.ontop_of.add(p)



root = filter(
    lambda x: len(x.ontop_of) == 0,
    programs.values())[0]

def whole_weight(p):
    s = p.weight
    p.subweights = {}
    for x in p.subs:
        p.subweights[x] = whole_weight(x)

    s += sum(p.subweights.values())
    if len(set(p.subweights.values())) > 1:
        print "problematic: %s" % p

    p.whole = s
    return s


