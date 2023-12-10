from grid_utils import *
with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)
start_y = ["S" in c for c in lines].index(True)
start_x = lines[start_y].index("S")
visited = [(start_y, start_x)]


def get_next(row, col):
    nexts = []
    nbs = neighbour_locations(len(lines), len(lines[0]), row, col)
    for nb in nbs:
        if nb[0] == row - 1 and lines[nb[0]][nb[1]] in "7F|" and lines[row][col] in "LJ|S":
            nexts.append(nb)
        elif nb[0] == row + 1 and lines[nb[0]][nb[1]] in "LJ|" and lines[row][col] in "7F|S":
            nexts.append(nb)
        elif nb[1] == col - 1 and lines[nb[0]][nb[1]] in "FL-" and lines[row][col] in "J7-S":
            nexts.append(nb)
        elif nb[1] == col + 1 and lines[nb[0]][nb[1]] in "J7-" and lines[row][col] in "FL-S":
            nexts.append(nb)
    return nexts


answer = 0
nexts = get_next(start_y, start_x)
while len(nexts) > 0:
    visited.extend(nexts)
    answer += 1
    new_nexts = []
    for next in nexts:
        new_nexts.extend(get_next(next[0], next[1]))
    nexts = [next for next in new_nexts if next not in visited]

print(answer)

# Remove unused pipe pieces
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (row, col) not in visited:
            g[row][col] = "."

# insert extra columns for squeezing
for row in range(len(lines)):
    to_insert = []
    for col in range(len(lines[0])):
        if g[row][col] in "FL-S" and g[row][col + 1] in "J7-S":
            to_insert.append("-")
        else:
            to_insert.append(".")
    new_row = [None] * (len(g[row]) + len(to_insert))
    new_row[::2] = g[row]
    new_row[1::2] = to_insert
    g[row] = new_row

# insert extra rows for squeezing
for row in range(len(g) - 2, -1, -1):
    new_row = []
    for col in range(len(g[0])):
        if g[row][col] in "7F|S" and g[row + 1][col] in "LJ|S":
            new_row.append("|")
        else:
            new_row.append(".")
    g.insert(row + 1, new_row)

#Add perimeter
for row in range(len(g)):
    g[row] = ["."] + g[row] + ["."]

g = [["."] * len(g[0])] + g + [["."] * len(g[0])]

#Find all outside parts (BFS)
outside = bfs_find_all(g, (0,0), ".")

for loc in outside:
    g[loc[0]][loc[1]] = "O"

#Remove extra rows and columns
g = g[1:len(g) - 1:2]
cols = len(g[0])
for row in range(len(g)):
    g[row] = g[row][1:cols - 1:2]

#All remaining empty spaces are inside
answer2 = 0
for row in g:
    answer2 += row.count(".")
print(answer2)
