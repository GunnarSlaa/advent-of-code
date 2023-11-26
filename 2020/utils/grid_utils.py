def grid_from_lines(input_lines):
    return [list(line) for line in input_lines]


def in_grid(grid_rows, grid_cols, loc):
    return 0 <= loc[0] < grid_rows  and 0 <= loc[1] < grid_cols


def neighbour_locations(grid_rows, grid_cols, row, col, diagonal=False):
    locations = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
    if diagonal:
        locations.extend([(row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)])
    return [loc for loc in locations if in_grid(grid_rows, grid_cols, loc)]


def neighbours(grid, row, col, diagonal=False):
    locations = neighbour_locations(len(grid), len(grid[0]), row, col, diagonal)
    nbs = [grid[r][c] for r, c in locations]
    return nbs


def print_grid(grid):
    for line in grid:
        print("".join(line))
