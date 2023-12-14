from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)


def roll_north(loc):
    while loc[0] != 0 and g[loc[0] - 1][loc[1]] == ".":
        g[loc[0] - 1][loc[1]] = "O"
        g[loc[0]][loc[1]] = "."
        loc[0] -= 1
    return(len(g) - loc[0])


answer = 0
for row in range(len(g)):
    for col in range(len(g[0])):
        if g[row][col] == "O":
            answer += roll_north([row, col])
print(answer)