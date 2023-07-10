#!/usr/bin/env python3

from pathlib import Path


def step(pots, rules):
    result = set()
    for i in range(min(pots) - 2, max(pots) + 3):
        w = "".join("#" if j in pots else "." for j in range(i - 2, i + 3))
        if rules[w] == "#":
            result.add(i)
    return result


lines = Path(Path(__file__).parent / "input12.txt").read_text().strip()
lines = lines.splitlines()
pots = set()
for i, c in enumerate(lines[0].split()[2]):
    if c == "#":
        pots.add(i)

rules = {}
for line in lines[2:]:
    rule, result = line.split(" => ")
    rules[rule] = result

s = pots
for i in range(20):
    s = step(s, rules)
part1 = sum(s)
print(f"Part 1: {part1}")

# Part 2
# This will only work if the pattern stabilizes, which it does.
s = pots
p = n = 0
for i in range(1000):
    p = n
    s = step(s, rules)
    n = sum(s)

part2 = (50000000000 - 1000) * (n - p) + n
print(f"Part 2: {part2}")
