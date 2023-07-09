#!/usr/bin/env python3

from pathlib import Path
import re


def state(points, t):
    return [(x + dx * t, y + dy * t) for x, y, dx, dy in points]


def bounds(points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    return min(xs), max(xs), min(ys), max(ys)


def area(points):
    minx, maxx, miny, maxy = bounds(points)
    return (maxx - minx) * (maxy - miny)


def min_area(points):
    t = 0
    while True:
        t += 1
        a = area(state(points, t))
        if a < area(state(points, t + 1)):
            return t


def display(points, t):
    minx, maxx, miny, maxy = bounds(state(points, t))
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x, y) in state(points, t):
                print("#", end="")
            else:
                print(".", end="")
        print()


lines = Path(Path(__file__).parent / "input10.txt").read_text().strip()
points = list()
for line in lines.split("\n"):
    x, y, dx, dy = map(int, re.findall(r"-?\d+", line))
    points.append((x, y, dx, dy))


part1 = min_area(points)
print(f"Part 1: {part1}")

display(points, 10630)
# print(f"Part 2: {part2}")
