import re
from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
total = 0
for row, line in enumerate(lines):
    matches = re.finditer("\d+", line)
    for m in matches:
        nbs = []
        for col in range(m.start(), m.end()):
            nbs.extend(neighbours(grid, row, col, True))
        if any(nb in "!@#$%^&*()-_=+/" for nb in nbs):
            total += int(m.group(0))

print(total)