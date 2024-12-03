from pathlib import Path
import aocd
import subprocess
import sys
import re


def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, lines)
    for match in matches:
        match = match.replace("mul", "").replace("(", "").replace(")", "").split(",")
        match = list(map(int, match))
        ans += match[0] * match[1]
    return ans


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matchidx = [(match.group(), match.start()) for match in re.finditer(pattern, lines)]
    do, dont = "do()", "don't()"
    dos, donts = [0], []
    for i in range(len(lines) - len(do)):
        if lines[i : len(do) + i] == do:
            dos.append(i)
    for i in range(len(lines) - len(dont)):
        if lines[i : len(dont) + i] == dont:
            donts.append(i)

    def checkidx(dos, donts, idx):
        smallestDo = 0
        smallestDont = -float("inf")
        for i in donts:
            if i > idx:
                break
            smallestDont = i
        for i in dos:
            if i > idx:
                break
            smallestDo = i
        return smallestDo > smallestDont

    for match in matchidx:
        match, idx = match
        match = match.replace("mul", "").replace("(", "").replace(")", "").split(",")
        match = list(map(int, match))
        if checkidx(dos, donts, idx):
            ans += match[0] * match[1]
    return ans


if __name__ == "__main__":
    day, year = aocd.get_day_and_year()
    result = subprocess.run(
        ["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    trimmed_lines = lines[3:-6]
    with Path(__file__).with_name("sample.txt").open("w") as sampleData:
        sampleData.write("\n".join(trimmed_lines))
    with Path(__file__).with_name("input.txt").open("w") as inputData:
        inputData.write(aocd.get_data(day=day, year=year))

    print(part1("sample.txt"))
    print(p1ans := part1())
    print(part2("sample.txt"))
    print(p2ans := part2())

    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            print(p1ans := part1())
            aocd.submit(p1ans)

        if sys.argv[1] == "2":
            print(p2ans := part2())
            aocd.submit(p2ans)
