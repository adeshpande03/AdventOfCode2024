from pathlib import Path
from collections import Counter

def part1(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    t = 0
    l1 = []
    l2 = []
    for line in lines:
        n1, n2 = int(line.split()[0]), int(line.split()[-1])
        l1.append(n1)
        l2.append(n2)
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        t += abs(l1[i] - l2[i])
    return t
    


def part2(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    t = 0
    l1 = []
    l2 = []
    for line in lines:
        n1, n2 = int(line.split()[0]), int(line.split()[-1])
        l1.append(n1)
        l2.append(n2)
    l2 = Counter(l2)
    for i in l1:
        t += i * l2[i]
    return t

if __name__ == "__main__":
    print(part1("sample.txt"))
    print(part1())
    print(part2("sample.txt"))
    print(part2())