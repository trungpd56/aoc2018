#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(points, p2=False):
    minx = min(p[0] for p in points)
    maxx = max(p[0] for p in points)
    miny = min(p[1] for p in points)
    maxy = max(p[1] for p in points)
    grid = defaultdict(list)
    infinite = set()
    region = set()
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            dists = [(dist((x, y), p), i) for i, p in enumerate(points)]
            dists = sorted(dists, key=lambda x: x[0])
            if dists[0][0] != dists[1][0]:
                grid[dists[0][1]].append((x, y))
            if x in (minx, maxx) or y in (miny, maxy):
                infinite.add(dists[0][1])
            if p2:
                if sum(d[0] for d in dists) < 10000:
                    region.add((x, y))
    if p2:
        return len(region)
    finite = set(range(len(points))) - infinite
    return max(len(grid[i]) for i in finite)


lines = Path(Path(__file__).parent / "input06.txt").read_text().strip()
points = []
for line in lines.split("\n"):
    x, y = map(int, line.split(", "))
    points.append((x, y))


part1 = solve(points)
print(f"Part 1: {part1}")
part2 = solve(points, True)
print(f"Part 2: {part2}")
