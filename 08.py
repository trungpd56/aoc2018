#!/usr/bin/env python3

from pathlib import Path


def solve(line):
    nchild, nmeta = next(line), next(line)
    children = [solve(line) for _ in range(nchild)]
    meta = [next(line) for _ in range(nmeta)]
    return meta, children


def sum_meta(node):
    meta, child = node
    return sum(meta) + sum(map(sum_meta, child))


line = Path(Path(__file__).parent / "input08.txt").read_text().strip()
# line = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
line = map(int, line.split())
root = solve(line)

part1 = sum_meta(root)
print(f"Part 1: {part1}")
part2 = ""
print(f"Part 2: {part2}")
