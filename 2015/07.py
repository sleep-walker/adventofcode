with open("07-input") as f:
    contents = f.read().splitlines()


def safe_int(x):
    try:
        return int(x)
    except:
        return x

class Node():
    target = None
    args = []
    value = None
    op = None

    def __init__(self, line):
        self.line = line
        source, self.target = line.split(" -> ", 1)
        ssplit = source.split(" ")
        if ssplit[0] == "NOT":
            self.op = "NOT"
            self.args = [safe_int(ssplit[1])]
        elif any([x in source for x in ("AND", "OR", "RSHIFT", "LSHIFT")]):
            self.op = ssplit[1]
            self.args = [safe_int(ssplit[0]), safe_int(ssplit[2])]
        elif len(ssplit) == 1:
            if source.isdigit():
                self.args = []
                self.value = int(source)
            else:
                self.args = [source]
                self.op = ":="
        else:
            raise Exception()

    def can_eval(self, values):
        return not [x for x in self.args if type(x) != int and x not in values]

    def eval(self, values):
        if not self.can_eval(values):
            return False
        args = [x if type(x) == int else values[x] for x in self.args]
        if self.op == "NOT":
            self.value = ~args[0]
        elif self.op == "AND":
            self.value = args[0] & args[1]
        elif self.op == "OR":
            self.value = args[0] | args[1]
        elif self.op == "LSHIFT":
            self.value = args[0] << args[1]
        elif self.op == "RSHIFT":
            self.value = args[0] >> args[1]
        elif self.op == ":=":
            self.value = args[0]
        if self.value < 0:
            self.value += 65536
        print(f"{self.target} <-- {self.value} ({self.line})")
        return True


class Nodes():
    def __init__(self, lines):
        self.nodes = []
        self.values = {}
        for l in lines:
            node = Node(l)
            if node.value:
                self.values.update({node.target: node.value})
            self.nodes.append(node)

    def add_node(self, l):
        node = Node(l)
        if node.value:
            self.values.update({node.target: node.value})
        self.nodes.append(node)
        return node

    def eval(self):
        changed = True
        while changed:
            changed = False
            for node in self.nodes:
                if node.target not in self.values and node.eval(self.values):
                    self.values.update({node.target: node.value})
                    changed = True
        return self

    def replace_node(self, l):
        node = self.add_node(l)
        old_nodes = [n for n in self.nodes if n.target == node.target and n != node]
        for on in old_nodes:
            self.nodes.remove(on)
        return self

assert Nodes([
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"]).eval().values == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456
    }

def part1():
    nodes = Nodes(contents)
    nodes.eval()
    return nodes.eval().values["a"]

def part2():
    nodes = Nodes(contents)
    nodes.replace_node("16076 -> b")
    return nodes.eval().values["a"]
