#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict


def solve(info, tasks):
    done = []
    while len(done) < len(tasks):
        for task in sorted(tasks):
            if info[task] <= set(done) and task not in done:
                done.append(task)
    return "".join(done)


def solve2(info, tasks):
    done = set()
    seconds = 0
    workers = [""] * 5
    counts = [0] * 5
    while True:
        for i, count in enumerate(counts):
            if count == 1:
                done.add(workers[i])
            counts[i] = max(0, count - 1)
        while 0 in counts:
            i = counts.index(0)
            candidates = [t for t in sorted(tasks) if info[t] <= set(done)]
            if not candidates:
                break
            task = min(candidates)
            tasks.remove(task)
            counts[i] = ord(task) - ord("A") + 61
            workers[i] = task
        if sum(counts) == 0:
            break
        seconds += 1

    return seconds


lines = Path(Path(__file__).parent / "input07.txt").read_text().strip()
info = defaultdict(set)
tasks = set()
for line in lines.splitlines():
    toks = line.split()
    tasks.update(toks[1], toks[7])
    info[toks[7]].add(toks[1])


part1 = solve(info, tasks)
print(f"Part 1: {part1}")
part2 = solve2(info, tasks)
print(f"Part 2: {part2}")
