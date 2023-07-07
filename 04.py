#!/usr/bin/env python3

from pathlib import Path
import re
from collections import defaultdict


def solve(lines):
    info = defaultdict(lambda: defaultdict(int))
    for line in lines:
        nums = list(map(int, re.findall(r"\d+", line)))
        if "#" in line:
            id = nums[-1]
        if "asleep" in line:
            start = nums[-1]
        if "wakes" in line:
            end = nums[-1]
            for i in range(start, end):
                info[id][i] += 1
    return info


lines = Path(Path(__file__).parent / "input04.txt").read_text().strip()
lines = sorted(lines.split("\n"))
info = solve(lines)

idmax = sorted(info, key=lambda x: sum(info[x].values()), reverse=True)[0]
minmax = sorted(info[idmax], key=lambda x: info[idmax][x], reverse=True)[0]
part1 = idmax * minmax
print(f"Part 1: {part1}")

idsame = sorted(info, key=lambda x: max(info[x].values()), reverse=True)[0]
minsame = sorted(info[idsame], key=lambda x: info[idsame][x], reverse=True)[0]
part2 = idsame * minsame
print(f"Part 2: {part2}")
