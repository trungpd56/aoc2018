#!/usr/bin/env python3

from pathlib import Path
from itertools import cycle


lines = Path(Path(__file__).parent / "input01.txt").read_text().strip()
nums = [int(line) for line in lines.splitlines()]

part1 = sum(nums)
print(f"Part 1: {part1}")

seen = set()
part2 = 0
for n in cycle(nums):
    part2 += n
    if part2 in seen:
        break
    seen.add(part2)

print(f"Part 2: {part2}")
