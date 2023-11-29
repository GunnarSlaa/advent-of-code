from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")


def neighbours(loc):
    return [(loc[0] + x, loc[1] + y, loc[2] + z, loc[3] + w) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in range(-1, 2) if not (x == y == z == w == 0)]


actives = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == "#":
            actives.append((x, y, 0, 0))

for _ in range(6):
    new_actives = set()
    to_check_set = set()
    for active in actives:
        to_check_set.update([nb for nb in neighbours(active)])
    for to_check in to_check_set:
        active_nbs = sum([nb in actives for nb in neighbours(to_check)])
        if active_nbs == 3 or to_check in actives and active_nbs == 2:
            new_actives.add(to_check)
    actives = new_actives
print(len(new_actives))
