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
result5 = 0
result6 = 0
result7 = 0
result8 = 0
for row in range(grid_rows):
    for col in range(grid_cols):
        if grid[row][col] == "X":
            if in_grid(grid_rows, grid_cols, (row, col + 1)) and grid[row][col + 1] == "M":
                if in_grid(grid_rows, grid_cols, (row, col + 2)) and grid[row][col + 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row, col + 3)) and grid[row][col + 3] == "S":
                        result += 1
                        result1 += 1
            if in_grid(grid_rows, grid_cols, (row+ 1, col + 1)) and grid[row + 1][col + 1] == "M":
                if in_grid(grid_rows, grid_cols, (row + 2, col + 2)) and grid[row + 2][col + 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row + 3, col + 3)) and grid[row + 3][col + 3] == "S":
                        result += 1
                        result2 += 1
            if in_grid(grid_rows, grid_cols, (row + 1, col)) and grid[row + 1][col] == "M":
                if in_grid(grid_rows, grid_cols, (row + 2, col)) and grid[row + 2][col] == "A":
                    if in_grid(grid_rows, grid_cols, (row + 3, col)) and grid[row + 3][col] == "S":
                        result += 1
                        result3 += 1
            if in_grid(grid_rows, grid_cols, (row - 1, col + 1)) and grid[row - 1][col + 1] == "M":
                if in_grid(grid_rows, grid_cols, (row - 2, col + 2)) and grid[row - 2][col + 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row - 3, col + 3)) and grid[row - 3][col + 3] == "S":
                        result += 1
                        result4 += 1
            if in_grid(grid_rows, grid_cols, (row+ 1, col - 1)) and grid[row + 1][col - 1] == "M":
                if in_grid(grid_rows, grid_cols, (row + 2, col - 2)) and grid[row + 2][col - 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row + 3, col - 3)) and grid[row + 3][col - 3] == "S":
                        result += 1
                        result5 += 1
            if in_grid(grid_rows, grid_cols, (row - 1, col - 1)) and grid[row - 1][col - 1] == "M":
                if in_grid(grid_rows, grid_cols, (row - 2, col - 2)) and grid[row - 2][col - 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row - 3, col - 3)) and grid[row - 3][col - 3] == "S":
                        result += 1
                        result6 += 1
            if in_grid(grid_rows, grid_cols, (row - 1, col)) and grid[row - 1][col] == "M":
                if in_grid(grid_rows, grid_cols, (row - 2, col)) and grid[row - 2][col] == "A":
                    if in_grid(grid_rows, grid_cols, (row - 3, col)) and grid[row - 3][col] == "S":
                        result += 1
                        result7 += 1
            if in_grid(grid_rows, grid_cols, (row, col - 1)) and grid[row][col - 1] == "M":
                if in_grid(grid_rows, grid_cols, (row, col - 2)) and grid[row][col - 2] == "A":
                    if in_grid(grid_rows, grid_cols, (row, col - 3)) and grid[row][col - 3] == "S":
                        result += 1
                        result8 += 1

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
