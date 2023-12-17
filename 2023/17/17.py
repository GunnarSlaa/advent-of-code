from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def neighbours(row, col, dir):
    nbs = []
    dirs_to_go = [(dir + 1) % 4, (dir + 3) % 4]
    for dir_to_go in dirs_to_go:
        cost = 0
        for i in range(1, 4):
            x = row + i * deltas[dir_to_go][0]
            y = col + i * deltas[dir_to_go][1]
            if not in_grid(len(g), len(g[0]), [x, y]):
                break
            cost += int(g[x][y])
            nbs.append((x, y, dir_to_go, cost))
    return nbs


unvisited = {
    (0, 0, 2): 0,
    (0, 0, 3): 0
}
visited = set()
current = (0, 0, 2)
while current[:2] != (len(g) - 1, len(g[0]) - 1):
    for nb in neighbours(current[0], current[1], current[2]):
        if nb[:3] in visited:
            continue
        if nb[:3] in unvisited.keys():
            unvisited[nb[:3]] = min(unvisited[nb[:3]], unvisited[current] + nb[3])
        else:
            unvisited[nb[:3]] = unvisited[current] + nb[3]
    visited.add(current)
    unvisited.pop(current)
    current = min(unvisited, key=unvisited.get)

print(unvisited[current])
