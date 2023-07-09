#!/usr/bin/env python3

from pathlib import Path


def reference(serial):
    info = {}
    for x in range(1, 301):
        for y in range(1, 301):
            info[(x, y)] = (((x + 10) * y + serial) * (x + 10) // 100) % 10 - 5
    return info


def grid(x, y, size=3):
    return sum(info[(x + dx, y + dy)] for dx in range(size) for dy in range(size))


def best(size):
    maxpower = 0
    maxcoord = (0, 0)
    for x in range(1, 301 - size):
        for y in range(1, 301 - size):
            power = grid(x, y, size)
            if power > maxpower:
                maxpower = power
                maxcoord = (x, y)
    return maxpower, maxcoord


def findsize():
    maxpower = 0
    maxcoord = (0, 0)
    maxsize = 1
    cnt = 0
    prev_power = 0
    for size in range(1, 301):
        power, coord = best(size)
        if power > maxpower:
            maxpower = power
            maxcoord = coord
            maxsize = size

        # use to eleminate early
        if power < prev_power:
            cnt += 1
        else:
            cnt = 0
        if cnt > 2:
            break
        prev_power = power

    return maxcoord, maxsize


line = Path(Path(__file__).parent / "input11.txt").read_text().strip()
serial = int(line)
# serial = 18
info = reference(serial)


part1 = best(3)
print(f"Part 1: {part1}")
part2 = findsize()
print(f"Part 2: {part2}")
