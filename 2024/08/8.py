from grid_utils import *
import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
antinodes = set()

for frequency in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    nodes = find_all_in_grid(frequency, grid)
    for pair in list(itertools.combinations(nodes, 2)):
        new_pairs = [(pair[0][0] - (pair[1][0] - pair[0][0]), pair[0][1] - (pair[1][1] - pair[0][1])), 
                     (pair[1][0] + (pair[1][0] - pair[0][0]), pair[1][1] + (pair[1][1] - pair[0][1]))]
        for new_pair in new_pairs:
            if in_grid(len(grid), len(grid[0]), new_pair):
                antinodes.add(new_pair)

print(len(antinodes))