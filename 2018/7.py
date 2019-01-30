#!/usr/bin/env python3

import logging
import copy

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("seven")

with open("/home/tcech/Stažené/adventofcode/7-input", "r") as f:
    lines = f.read().splitlines()

class Step(object):

    def __init__(self):
        self.after = set()
        self.before = set()
        self.done = False

    def add_before(self, x):
        if self.before is None:
            self.before = set()
        self.before.add(x)

    def add_after(self, x):
        if self.after is None:
            self.after = set()
        self.after.add(x)

    def remove_before(self, x):
        # if x in self.before:
        #     self.before.remove(x)
        self.before = self.before.difference(set(x))

    def ready(self):
        return len(self.before) == 0

class StepList(object):
    steps = {}

    order = ''
    _free_steps = None

    def __init__(self):
        self.working_on = set()

    def add_rule(self, s):
        #s[5] before s[36]
        f = s[5]
        t = s[36]
        log.debug("%s --> %s" % (f, t))
        first = self.steps.get(f, Step())
        first.add_after(t)
        self.steps[f] = first

        then = self.steps.get(t, Step())
        then.add_before(f)
        self.steps[t] = then

    def make_done(self, s):
        log.debug("%s is now done", s)
        self.order += s
        self._free_steps = None
        self.steps[s].done = True
        self.working_on.remove(s)
        for name, val in self.steps.items():
            val.remove_before(s)

    @property
    def free_steps(self):
        if self._free_steps is None:
            self._free_steps = sorted(
            [name for name, obj in self.steps.items() if obj.ready() and not obj.done]
            )
        return self._free_steps

    def get_next_step(self):
        if len(self.free_steps) == 0:
            return None
        else:
            n = [i for i in self.free_steps if i not in self.working_on][0]
            self.working_on.add(n)
            return n

    def cont(self):
        return len(self.free_steps) > 0

sl = StepList()

#class Schedule(object):


def add_rules():
    for l in lines:
        sl.add_rule(l)


def do_steps_one():
    x = sl.get_next_step()
    while sl.cont():
        sl.make_done(x)
        x = sl.get_next_step()

add_rules()
do_steps_one()
print("Order: %s" % sl.order)

def do_steps_two():
    t = 0
    # 4 elves at the same time
    free_elves = set(range(4))
    pass
