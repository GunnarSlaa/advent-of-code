def grid_from_lines(input_lines):
    return [list(line) for line in input_lines]


def in_grid(grid_rows, grid_cols, loc):
    return 0 <= loc[0] < grid_rows and 0 <= loc[1] < grid_cols

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = grid_from_lines(lines)
grid_rows = len(grid)
grid_cols = len(grid[0])
result = 0
result1 = 0
result2 = 0
result3 = 0
result4 = 0
for row in range(grid_rows):
    for col in range(grid_cols):
        if grid[row][col] == "A":
            if in_grid(grid_rows, grid_cols, (row + 1, col + 1)) and grid[row + 1][col + 1] == "M":
                if in_grid(grid_rows, grid_cols, (row + 1, col - 1)) and grid[row + 1][col - 1] == "M":
                    if in_grid(grid_rows, grid_cols, (row - 1, col - 1)) and grid[row - 1][col - 1] == "S":
                        if in_grid(grid_rows, grid_cols, (row - 1, col + 1)) and grid[row - 1][col + 1] == "S":
                            result += 1
                            result1 += 1
            if in_grid(grid_rows, grid_cols, (row + 1, col + 1)) and grid[row + 1][col + 1] == "S":
                if in_grid(grid_rows, grid_cols, (row + 1, col - 1)) and grid[row + 1][col - 1] == "M":
                    if in_grid(grid_rows, grid_cols, (row - 1, col - 1)) and grid[row - 1][col - 1] == "M":
                        if in_grid(grid_rows, grid_cols, (row - 1, col + 1)) and grid[row - 1][col + 1] == "S":
                            result += 1
                            result2 += 1
            if in_grid(grid_rows, grid_cols, (row + 1, col + 1)) and grid[row + 1][col + 1] == "S":
                if in_grid(grid_rows, grid_cols, (row + 1, col - 1)) and grid[row + 1][col - 1] == "S":
                    if in_grid(grid_rows, grid_cols, (row - 1, col - 1)) and grid[row - 1][col - 1] == "M":
                        if in_grid(grid_rows, grid_cols, (row - 1, col + 1)) and grid[row - 1][col + 1] == "M":
                            result += 1
                            result3 += 1
            if in_grid(grid_rows, grid_cols, (row + 1, col + 1)) and grid[row + 1][col + 1] == "M":
                if in_grid(grid_rows, grid_cols, (row + 1, col - 1)) and grid[row + 1][col - 1] == "S":
                    if in_grid(grid_rows, grid_cols, (row - 1, col - 1)) and grid[row - 1][col - 1] == "S":
                        if in_grid(grid_rows, grid_cols, (row - 1, col + 1)) and grid[row - 1][col + 1] == "M":
                            result += 1
                            result4 += 1

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
