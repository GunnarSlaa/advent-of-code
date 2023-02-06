import re

with open("input", "r") as f:
    lines = f.read().split("\n")

def neighbour(direction, cell):
    if direction == 0:
        direct = (cell[0], cell[1] - 1)
        if direct in grid: return direct
        else: return (cell[0], colSizes[cell[0]][1])
    if direction == 1:
        direct = (cell[0] + 1, cell[1])
        if direct in grid: return direct
        else: return (rowSizes[cell[1]][0], cell[1])
    if direction == 2:
        direct = (cell[0], cell[1] + 1)
        if direct in grid: return direct
        else: return (cell[0], colSizes[cell[0]][0])
    if direction == 3:
        direct = (cell[0] - 1, cell[1])
        if direct in grid: return direct
        else: return (rowSizes[cell[1]][1], cell[1])

def move(direction, cell):
    nb = neighbour(direction, cell)
    if nb in grid:
        return grid[nb] == '.'
    else: print("PANIC!!")

def turn(direction, LR):
    if LR == "R": return (direction + 1) % 4
    else: return (direction + 3) % 4

length = max([len(line) for line in lines[:-2]])
rowSizes = []
colSizes = []
grid = {}
for row, line in enumerate(lines[:-2]):
    size = [len(re.split('#|\.', line)[0]), len(line) - 1]
    rowSizes.append(size)
    for col in range(size[0], size[1] + 1):
        grid[(col, row)] = line[col]
for col in range(length):
    start = min([tup[1] for tup in grid if tup[0] == col])
    end = max([tup[1] for tup in grid if tup[0] == col])
    colSizes.append([start, end])

pos = (8,0)
face = 1

moves = re.split('R|L', lines[-1])
turns = [_ for _ in re.split('\d', lines[-1]) if _ != '']
print(len(moves), len(turns))
print(moves)
for nextMove in range(len(moves)):
    for _ in range(int(moves[nextMove])):
        if move(face, pos):
            pos = neighbour(face, pos)
        else:
            break
    if nextMove != len(moves) - 1: face = turn(face, turns[nextMove])
print((1000 * (pos[1] + 1)) + (4 * (pos[0] + 1)) + ((face + 3) % 4))