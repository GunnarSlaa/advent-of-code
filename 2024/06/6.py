from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
visited = set()

pos = find_in_grid("^", grid)
direction = 0

while in_grid(len(grid), len(grid[0]), pos):
    visited.add(pos)
    facing = get_neighbour_dir(grid, pos[0], pos[1], direction)
    if facing == None:
       break
    if not check_grid(grid, facing[0], facing[1], "#"):
        pos = facing
    else:
        direction = (direction + 1) % 4

print(len(visited))