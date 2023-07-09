#!/usr/bin/env python3

from pathlib import Path


def solve(line):
    result = [""]
    for c in line:
        if c == result[-1].swapcase():
            result.pop()
        else:
            result.append(c)
    return "".join(result)


def solve2(line):
    best = len(line)
    for c in set(line.lower()):
        nline = line.replace(c, "").replace(c.upper(), "")
        best = min(best, len(solve(nline)))
    return best


line = Path(Path(__file__).parent / "input05.txt").read_text().strip()

# line = "dabAcCaCBAcCcaDA"
part1 = len(solve(line))
print(f"Part 1: {part1}")
part2 = solve2(line)
print(f"Part 2: {part2}")
