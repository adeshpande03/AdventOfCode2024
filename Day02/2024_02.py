from pathlib import Path
import aocd
import subprocess

def part1(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    
    for l in lines:
        l = list(map(int, l.split()))
        if l == list(sorted(l)):
            if all(1 <= l[i] - l[i - 1] <= 3 for i in range(1, len(l))):
                ans += 1
        elif l == list(sorted(l, reverse=True)):
            if all(-1 >= l[i] - l[i - 1] >= -3 for i in range(1, len(l))):
                ans += 1
        
    return ans


def part2(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    
    ans = 0
    def safe(l):
        if l == list(sorted(l)):
            if all(1 <= l[i] - l[i - 1] <= 3 for i in range(1, len(l))):
                return 1
        elif l == list(sorted(l, reverse=True)):
            if all(-1 >= l[i] - l[i - 1] >= -3 for i in range(1, len(l))):
                return 1
    for l in lines:
        l = list(map(int, l.split()))
        for i in range(len(l)):
            newL = l[:i] + l[i+1:]
            if safe(newL):
                ans += 1
                break
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
    
    # aocd.submit(p1ans)
    # aocd.submit(p2ans)
