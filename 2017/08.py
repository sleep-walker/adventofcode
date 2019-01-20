import logging

registers = {}
log = logging.getLogger()

class Instr(object):
    def __init__(self, expression, condition):
        log.debug("creating instruction with ex '%s' and cond '%s'",
                  expression, condition)
        self.construct_lexpr(expression)
        self.construct_lcond(condition)
        if self.lcond():
            self.lexpr()

    def construct_lexpr(self, ex):
        elements = ex.split(" ")
        expr = "lambda : registers.update({'%s': registers.get('%s', 0) %s (%s)})" % (
            elements[0], elements[0],
            elements[1].replace("dec", "-").replace("inc", "+"),
            elements[2])
        log.debug("creating condition: %s", expr)
        self.lexpr = eval(expr)

    def construct_lcond(self, condition):
        a, operator, b = condition.split(" ")
        ops = []
        for i in (a, b):
            try:
                op = int(i)
            except ValueError:
                op = "registers.get('%s', 0)" % i
            ops.append(op)
        cond = "lambda : %s %s %s" % (ops[0], operator, ops[1])
        log.debug("creating condition: %s", cond)
        self.lcond = eval(cond)

def read_input(l):
    ex, cond = l.split(" if ")
    return Instr(ex, cond)

with open("08-input", "r") as f:
    lines = f.read().splitlines()

m = []
for l in lines:
    x = read_input(l)
    if registers:
        m.append(max(registers.values()))

print max(registers.values())
print max(m)
