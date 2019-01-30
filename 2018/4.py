#!/usr/bin/env python3

import datetime
import operator
import io
from collections import Counter
import copy
import logging

log = logging.getLogger("four")
log.setLevel(logging.DEBUG)

with open("/home/tcech/Stažené/adventofcode/4-input", "r") as f:
    lines = f.read().splitlines()


class Entry(object):
    ts = None
    event = None
    guard = -1
    SLEEP = 0
    WAKE = 1
    SWITCH = 2
    def __init__(self, s):
        assert(s[0] == "[")
        s = s[1:]
        ts, s = s.split("] ", 1)
        self.ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M")
        if s == "wakes up":
            self.event = self.WAKE
        elif s == "falls asleep":
            self.event = self.SLEEP
        elif "Guard " in s and "begins shift" in s:
            self.event = self.SWITCH
            _, s = s.split("#", 1)
            guard, _ = s.split(" ", 1)
            self.guard = int(guard)
        else:
            raise Exception("Error on input: %s")

    def __str__(self):
        if self.event == self.SLEEP:
            es = "falls asleep"
        elif self.event == self.WAKE:
            es = "wakes up"
        elif self.event == self.SWITCH:
            es = "Guard #%d begins shift" % self.guard
        else:
            raise Exception("WAT?!")

        return "[%s] %s" % (self.ts.strftime("%Y-%m-%d %H:%M"), es)

class Guard(object):
    gid = -1
    intervals = None
    _mins = None
    _sum = None

    def __init__(self, gid):
        self.gid = gid

    # def __str__(self):
    #     return "guard #%d" % self.gid

    # def __repr__(self):
    #     return str(self)

    def add_interval(self, start, end):
        if self.intervals is None:
            self.intervals = []
        self.intervals.append((start, end))

    @property
    def sum_mins(self):
        if self._sum is None:
            self._sum = 0
            for i in self.intervals:
                self._sum += (i[1] - i[0]).seconds // 60

        return self._sum

    @sum_mins.setter
    def sum_mins(self, s):
        pass

    def get_mins(self):
        if self._mins is None:
            self._mins = []
            for i in self.intervals:
                self._mins += [
                    min % 60
                    for min in range(i[0].minute, i[1].minute)]
        return self._mins

    @property
    def mins(self):
        return self.get_mins()

    @mins.setter
    def mins(self, mins):
        _mins = mins

    def __gt__(self, x):
        return self.sum_mins > x.sum_mins
    def __ge__(self, x):
        return self.sum_mins >= x.sum_mins
    def __lt__(self, x):
        return self.sum_mins < x.sum_mins
    def __le__(self, x):
        return self.sum_mins <= x.sum_mins

class GuardLog(object):
    events = []
    guards = {}
    def read_entry(self, s):
        self.events.append(Entry(s))

    def sort(self):
        self.events.sort(key=operator.attrgetter("ts"))

    def __str__(self):
        with io.StringIO() as out:
            out.write("guard log:\n")
            for i in self.events:
                out.write(str(i) + "\n")
            output = out.getvalue()
        return output

    def process(self):
        start = None
        end = None
        g = -1
        for i in self.events:
            log.debug("Processing event: %s", i)
            if i.event == Entry.SWITCH:
                g = i.guard
            elif i.event == Entry.SLEEP:
                start = i.ts
            elif i.event == Entry.WAKE:
                end = i.ts
                gg = self.guards.get(g, Guard(g))
                log.debug("Guard #%d (%s): adding interval (%s - %s)", gg.gid, gg, start, end)
                if g not in self.guards:
                    self.guards[g] = gg
#                gg.intervals += [(start, end)]
                gg.add_interval(start, end)
#                self.guards[g].add_interval(start, end)


def most_common(lst):
    data = Counter(lst)
    x = data.most_common(1)[0]
    return x

gl = GuardLog()

for i in lines:
    gl.read_entry(i)

gl.sort()
#print(gl)
gl.process()

# most sleeping guard
guard = sorted(
    gl.guards.values(), key=operator.attrgetter("sum_mins"), reverse=True)[0]

# minutes when he sleeps
data = Counter(guard.mins)
print("guard %s slept %d minutes" % (guard.gid, data.most_common(1)[0][0]))

# gather all minutes
mins = []
for i in gl.guards.values():
    mins += i.mins
data = Counter(mins)
# most common minute
minute = data.most_common(1)[0][0]

sleeper = sorted([(most_common(i.mins), i) for i in gl.guards.values()], key=lambda x: x[0][1], reverse=True)[0]

print("guard %s is sleeping most often on %d minute" % (sleeper[1].gid, sleeper[0][0]))
