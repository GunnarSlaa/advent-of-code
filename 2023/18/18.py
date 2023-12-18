from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)
deltas = { "U": (-1, 0),
           "R": (0, 1),
           "D": (1, 0),
           "L": (0, -1)}

loc = (0, 0)
nodes = [loc]
border = 0
for line in lines:
    dir = deltas[line.split()[0]]
    amount = int(line.split()[1])
    x = loc[0] + amount * dir[0]
    y = loc[1] + amount * dir[1]
    loc = (x, y)
    nodes.append(loc)
    border += amount

nodes.append((0,0))
nodes = nodes[::-1]
shoelace = 0
for i in range(len(nodes) - 1):
    shoelace += nodes[i][0] * nodes[i + 1][1]
    shoelace -= nodes[i][1] * nodes[i + 1][0]

print(shoelace)
print(shoelace / 2 + border / 2 + 1)
print(border)
