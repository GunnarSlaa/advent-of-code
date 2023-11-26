import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

grid = [list(line) for line in lines]


def slope(dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(grid):
        if grid[y][x % len(grid[y])] == "#":
            trees += 1
        x += dx
        y += dy
    return trees


print(slope(3, 1))
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
