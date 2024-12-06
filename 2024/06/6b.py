def check_grid_loop(grid):
    visited = set()
    pos = find_in_grid("^", grid)
    direction = 0

    while in_grid(len(grid), len(grid[0]), pos):
        new_tuple = (pos[0], pos[1], direction)
        if new_tuple in visited:
            return 1
        visited.add(new_tuple)
        facing = get_neighbour_dir(grid, pos[0], pos[1], direction)
        if facing == None:
            return 0
        if not check_grid(grid, facing[0], facing[1], "#"):
            pos = facing
        else:
            direction = (direction + 1) % 4


from grid_utils import *
from copy import deepcopy

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

orig_grid = grid_from_lines(lines)
result = 0

for row in range(len(orig_grid)):
    for col in range(len(orig_grid[0])):
        if orig_grid[row][col] == "#":
            continue
        if orig_grid[row][col] == "^":
            continue
        grid = deepcopy(orig_grid)
        grid[row][col] = "#"
        result += check_grid_loop(grid)
        

print(result)