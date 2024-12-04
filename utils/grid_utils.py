def grid_from_lines(input_lines):
    return [list(line) for line in input_lines]


def in_grid(grid_rows, grid_cols, loc):
    return 0 <= loc[0] < grid_rows and 0 <= loc[1] < grid_cols


def check_grid(grid, row, col, value):
    if not in_grid(len(grid), len(grid[0]), (row, col)):
        return False
    return grid[row][col] == value


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


def bfs_find_all(g, start, to_find):
    frontier = [start]
    found = []
    while len(frontier) > 0:
        new_frontier = set()
        for loc in frontier:
            new_frontier.update(neighbour_locations(len(g), len(g[0]), loc[0], loc[1]))
        new_frontier = [loc for loc in new_frontier if loc not in frontier and loc not in found]
        new_frontier = [loc for loc in new_frontier if g[loc[0]][loc[1]] in to_find]
        found.extend(frontier)
        frontier = new_frontier
    return found


def get_neighbour_dir(g, row, col, dir):
    locations = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
    return locations[dir] if in_grid(len(g), len(g[0]), locations[dir]) else None
