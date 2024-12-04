from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
result = 0
directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "X":
            for direction in directions:
                if check_grid(grid, row + direction[0], col + direction[1], "M"):
                    if check_grid(grid, row + 2 * direction[0], col + 2 * direction[1], "A"):
                        if check_grid(grid, row + 3 * direction[0], col + 3 * direction[1], "S"):
                            result += 1

print(result)