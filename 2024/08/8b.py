from grid_utils import *
import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
antinodes = set()

for frequency in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    nodes = find_all_in_grid(frequency, grid)
    for pair in list(itertools.combinations(nodes, 2)):
        antinode = (pair[0])
        inc = 0
        while in_grid(len(grid), len(grid[0]), antinode):
            antinodes.add(antinode)
            inc += 1
            antinode = (pair[0][0] - inc * (pair[1][0] - pair[0][0]), pair[0][1] - inc * (pair[1][1] - pair[0][1]))
        antinode = (pair[1])
        inc = 0
        while in_grid(len(grid), len(grid[0]), antinode):
            antinodes.add(antinode)
            inc += 1
            antinode = (pair[1][0] + inc * (pair[1][0] - pair[0][0]), pair[1][1] + inc * (pair[1][1] - pair[0][1]))

print(len(antinodes))