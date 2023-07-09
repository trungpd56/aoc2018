#!/usr/bin/env python3

from pathlib import Path
from collections import deque
import re


def solve(players, num_marbles):
    queue = deque([0])
    scores = [0] * players
    for n in range(1, num_marbles + 1):
        if n % 23 == 0:
            queue.rotate(7)
            scores[n % players] += n + queue.pop()
            queue.rotate(-1)
        else:
            queue.rotate(-1)
            queue.append(n)
    return max(scores)


lines = Path(Path(__file__).parent / "input09.txt").read_text().strip()
players, num_marbles = map(int, re.findall(r"\d+", lines))


part1 = solve(players, num_marbles)
print(f"Part 1: {part1}")
part2 = solve(players, num_marbles * 100)
print(f"Part 2: {part2}")
