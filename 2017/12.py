import logging

log = logging.getLogger()
log.setLevel(logging.WARN)

class EqGroups(object):
    d = {}
    def __init__(self):
        pass

    def d_merge(self, g1, g2):
        for k in self.d.keys():
            if self.d[k] == g2:
                self.d[k] = g1

    def d_set_group(self, pids, group):
        for p in pids:
            self.d[p] = group

    def d_add_line(self, elem, links):
        log.debug('elem + links = %s', [elem]+links)
        groups = set()
        for i in [elem] + links:
            if i in self.d.keys():
                groups.add(self.d[i])

        groups = list(groups)
        if len(groups) == 0:
            # create new group elem
            self.d_set_group([elem] + links, elem)
        elif len(groups) == 1:
            # add to existing group
            self.d_set_group([elem] + links, groups[0])
        else:
            # more than 1 group - merge
            for g in groups[1:]:
                self.d_merge(groups[0], g)
            # and add to the group
            self.d_set_group([elem] + links, groups[0])

    def len_group_zero(self):
        return len([x for x in e.d if e.d[x] == e.d['0']])

    def number_groups(self):
        return len(set(e.d.values()))

e = EqGroups()
def line(s):
    e, rest = s.split(" <-> ")
    links = rest.split(", ")
    return e, links


# test_input = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
# """

# lines = test_input.splitlines()

with open("12-input", "r") as f:
    lines = f.read().splitlines()

for l in lines:
    e.d_add_line(*line(l))

print e.len_group_zero()
print e.number_groups()
