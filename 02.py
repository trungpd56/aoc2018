#!/usr/bin/env python3

from pathlib import Path


def solve(lines):
    cnt2, cnt3 = 0, 0
    for line in lines:
        if any(line.count(c) == 2 for c in line):
            cnt2 += 1
        if any(line.count(c) == 3 for c in line):
            cnt3 += 1
    return cnt2 * cnt3


def solve2(lines):
    for line1 in lines:
        for line2 in lines:
            if line1 == line2:
                continue
            diff = 0
            for i, c in enumerate(line1):
                if c != line2[i]:
                    diff += 1
            if diff == 1:
                return "".join(c for i, c in enumerate(line1) if line1[i] == line2[i])


lines = Path(Path(__file__).parent / "input02.txt").read_text().strip()
lines = lines.split("\n")

part1 = solve(lines)
print(f"Part 1: {part1}")
part2 = solve2(lines)
print(f"Part 2: {part2}")
