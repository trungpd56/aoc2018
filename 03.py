#!/usr/bin/env python3

from pathlib import Path
import re
from collections import defaultdict


lines = Path(Path(__file__).parent / "input03.txt").read_text().strip()
info = defaultdict(list)
for line in lines.splitlines():
    id, x, y, w, h = map(int, re.findall(r"\d+", line))
    for i in range(x, x + w):
        for j in range(y, y + h):
            info[(i, j)].append(id)

part1 = sum(1 for v in info.values() if len(v) > 1)
print(f"Part 1: {part1}")

all_ids = set()
invalid_ids = set()
for x in info.values():
    all_ids.update(x)
    if len(x) > 1:
        invalid_ids.update(x)

part2 = (all_ids - invalid_ids).pop()
print(f"Part 2: {part2}")
