from pathlib import Path
import aocd
import subprocess
import sys


def part1(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    for line in range(len(lines)):
        lines[line] = list(lines[line].strip())
    ans = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != "X":
                continue
            for dx, dy in [(-1,1), (1, 1), (1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1)]:
                xx, yy = x + dx, y + dy
                s = ""
                while (
                    xx >= 0
                    and xx < len(lines[0])
                    and yy >= 0
                    and yy < len(lines)
                    and len(s) < 3
                ):
                    s += lines[yy][xx]
                    xx += dx
                    yy += dy
                if s == "MAS":
                    ans += 1
    return ans


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != "A" or x == 0 or y == 0 or y == len(lines) - 1 or x == len(lines[0]) - 1:
                continue

            tr, br, tl, bl = (
                lines[y - 1][x + 1],
                lines[y + 1][x + 1],
                lines[y - 1][x - 1],
                lines[y + 1][x - 1],
            )
            if (tr + bl) in ("MS", "SM") and (tl + br) in ("MS", "SM"):
                ans += 1
    return ans


if __name__ == "__main__":
    day, year = aocd.get_day_and_year()
    result = subprocess.run(
        ["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    trimmed_lines = lines[3:-6]
    # with Path(__file__).with_name("sample.txt").open("w") as sampleData:
    #     sampleData.write("\n".join(trimmed_lines))
    with Path(__file__).with_name("input.txt").open("w") as inputData:
        inputData.write(aocd.get_data(day=day, year=year))

    print(part1("sample.txt"))
    print(p1ans := part1())
    print(part2("sample.txt"))
    print(p2ans := part2())

    if len(sys.argv) > 1:
        if sys.argv[1] == '1':
            print(p1ans := part1())
            aocd.submit(p1ans)

        if sys.argv[1] == '2':
            print(p2ans := part2())
            aocd.submit(p2ans)
        
