from pathlib import Path
from collections import Counter
from aocd import get_data, submit
import subprocess


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
    day = 1
    year = 2024
    
    result = subprocess.run(
        ["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    trimmed_lines = lines[3:-6]
    with Path(__file__).with_name("sample.txt").open("w") as sampleData:
        sampleData.write("\n".join(trimmed_lines))
    with Path(__file__).with_name("input.txt").open("w") as inputData:
        inputData.write(get_data(day=day, year=year))
        
    print(part1("sample.txt"))
    print(p1ans := part1())
    print(part2("sample.txt"))
    print(p2ans := part2())
    
    # submit(p1ans)
    # submit(p2ans)
