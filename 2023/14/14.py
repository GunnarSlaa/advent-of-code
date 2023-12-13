from grid_utils import *
from itertools import combinations

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)

galaxies = []
for row in range(len(g)):
    for col in range(len(g[0])):
        if g[row][col] == "#":
            galaxies.append((row, col))


def solve(exp_size):
    answer = 0

    for row in range(len(g) - 2, -1, -1):
        if "#" not in g[row]:
            up = len([galaxy for galaxy in galaxies if galaxy[0] < row])
            down = len([galaxy for galaxy in galaxies if galaxy[0] > row])
            answer += up * down * (exp_size - 1)

    for col in range(len(g[0]) - 2, -1, -1):
        if not any([row[col] == "#" for row in g]):
            left = len([galaxy for galaxy in galaxies if galaxy[1] < col])
            right = len([galaxy for galaxy in galaxies if galaxy[1] > col])
            answer += left * right * (exp_size - 1)

    pairs = list(combinations(galaxies, 2))
    for pair in pairs:
        answer += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

    return answer


print(solve(2))
print(solve(1_000_000))