import re
from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
gears = {}
for row, line in enumerate(lines):
    matches = re.finditer("\d+", line)
    for m in matches:
        nbs = []
        for col in range(m.start(), m.end()):
            nbs.extend(neighbour_locations(len(grid), len(grid[0]), row, col, True))
        nbs = set(nbs)
        for nb in nbs:
            if grid[nb[0]][nb[1]] == "*":
                if nb in gears.keys():
                    gears[nb].append(int(m.group(0)))
                else:
                    gears[nb] = [int(m.group(0))]

total = 0
for i in gears.values():
    if len(i) == 2:
        total += i[0] * i[1]
print(total)