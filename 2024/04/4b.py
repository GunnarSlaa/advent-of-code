from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
result = 0
cornerstrings = ["MMSS", "SMMS", "SSMM", "MSSM"]
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "A":
            for cornerstring in cornerstrings:
                if check_grid(grid, row + 1, col + 1, cornerstring[0]):
                    if check_grid(grid, row + 1, col - 1, cornerstring[1]):
                        if check_grid(grid, row - 1, col - 1, cornerstring[2]):
                            if check_grid(grid, row - 1, col + 1, cornerstring[3]):
                                result += 1

print(result)
