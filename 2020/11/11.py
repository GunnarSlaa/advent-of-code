from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
num_rows = len(grid)
num_cols = len(grid[0])
while True:
    becomes_empty = []
    becomes_occupied = []
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == "L" and "#" not in neighbours(grid, row, col, True):
                becomes_occupied.append((row,col))
            elif grid[row][col] == "#" and neighbours(grid, row, col, True).count("#") >= 4:
                becomes_empty.append((row,col))
    if len(becomes_occupied) == 0 and len(becomes_empty) == 0:
        break
    for o in becomes_occupied:
        grid[o[0]][o[1]] = "#"
    for e in becomes_empty:
        grid[e[0]][e[1]] = "L"

print(sum([row.count("#") for row in grid]))


def view(row, col, dhor, dver):
    target = (row + dver, col + dhor)
    while in_grid(num_rows, num_cols, target) and grid[target[0]][target[1]] == ".":
        target = (target[0] + dver, target[1] + dhor)
    if in_grid(num_rows, num_cols, target):
        return grid[target[0]][target[1]]
    else:
        return None


def view_all(row, col):
    seen = []
    for dhor in range(-1, 2):
        for dver in range(-1, 2):
            if dver == dhor == 0: continue
            s = view(row, col, dhor, dver)
            if s: seen.append(s)
    return seen


grid = grid_from_lines(lines)
while True:
    becomes_empty = []
    becomes_occupied = []
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == "L" and "#" not in view_all(row, col):
                becomes_occupied.append((row,col))
            elif grid[row][col] == "#" and view_all(row, col).count("#") >= 5:
                becomes_empty.append((row,col))
    if len(becomes_occupied) == 0 and len(becomes_empty) == 0:
        break
    for o in becomes_occupied:
        grid[o[0]][o[1]] = "#"
    for e in becomes_empty:
        grid[e[0]][e[1]] = "L"

print(sum([row.count("#") for row in grid]))
