import re

from collections import defaultdict


with open("07-input") as f:
    str_lines = f.read().splitlines()


leaf_r = re.compile("(\w+) (\w+) bags contain no other bags.")
r = re.compile("shiny gold bags contain (([0-9]+) (\w+) (\w+) bags?, )*([0-9]+) (\w+) (\w+) bags?.")

def build_tree(lines):
    tree = defaultdict(lambda: None)
    for l in lines:
        if leaf_r.match(l):
            tree
