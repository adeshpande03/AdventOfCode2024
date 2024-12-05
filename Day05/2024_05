from pathlib import Path
# import aocd
import subprocess
import sys
import re
from collections import defaultdict, Counter, deque
from collections import defaultdict
from functools import total_ordering
def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    p1 = lines.split("\n\n")[0]
    p1 = p1.split("\n")
    p2 = lines.split("\n\n")[-1]
    p2 = p2.split("\n")
    rules = [i.split('|') for i in p1]
    print(rules)
    rules = [(int(i[0]), int(i[1])) for i in rules]
    def t(line, rules = rules):
        for i in rules:
            if i[0] in line and i[1] in line:
                if not line.index(i[0]) < line.index(i[1]):
                    return False
        return True
    for line in p2:
        line = list(map(int, line.split(',')))
        print(line)
        if t(line):
            ans += line[len(line)//2]

    return ans



def part2(filename="input.txt"): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    orderings = []
    pairs = {}
    i = 0
    while lines[i] != '':
        n0, n1 = lines[i].split('|')
        if n1 not in pairs:
            pairs[n1] = [n0]
        else:
            pairs[n1].append(n0)
        i += 1
    i += 1
    while i < len(lines):
        orderings.append(lines[i].split(','))
        i += 1
        
    @total_ordering
    class num_comp:
        def __init__(self, s):
            self.s = s
        def __eq__(self, other):
            if self.s in pairs:
                return other.s not in pairs[self.s]
            if other.s in pairs:
                return self.s not in pairs[other.s]
            return True
        def __lt__(self, other):
            if self.s not in pairs: return False
            return other.s in pairs[self.s]
        
    bad_orders = []
    for order in orderings:
        for i in range(len(order)):
            if order[i] not in pairs: continue
            for j in range(i+1, len(order)):
                if order[j] in pairs[order[i]]: break
            else: continue
            break
        else: continue
        bad_orders.append([num_comp(o) for o in order])
    out = 0
    for o in bad_orders:
        o = sorted(o)
        out += int(o[len(o)//2].s)
    print(out)



if __name__ == "__main__":
    # print(part1("sample.txt"))
    # print(part1())
    # print(part2("sample.txt"))
    # print(part2())
        
