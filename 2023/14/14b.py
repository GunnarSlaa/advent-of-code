from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)
cycles = 1_000_000_000


def roll_north(loc):
    while loc[0] != 0 and g[loc[0] - 1][loc[1]] == ".":
        g[loc[0] - 1][loc[1]] = "O"
        g[loc[0]][loc[1]] = "."
        loc[0] -= 1
    return len(g) - loc[0]


def roll_east(loc):
    while loc[1] != len(g[0]) - 1 and g[loc[0]][loc[1] + 1] == ".":
        g[loc[0]][loc[1] + 1] = "O"
        g[loc[0]][loc[1]] = "."
        loc[1] += 1
    return loc[1]


def roll_south(loc):
    while loc[0] != len(g) - 1 and g[loc[0] + 1][loc[1]] == ".":
        g[loc[0] + 1][loc[1]] = "O"
        g[loc[0]][loc[1]] = "."
        loc[0] += 1
    return loc[0]


def roll_west(loc):
    while loc[1] != 0 and g[loc[0]][loc[1] - 1] == ".":
        g[loc[0]][loc[1] - 1] = "O"
        g[loc[0]][loc[1]] = "."
        loc[1] -= 1
    return len(g[0]) - loc[1]


def cycle():
    cycle_outcome = []
    #North
    load = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                load += roll_north([row, col])
    cycle_outcome.append(load)
    # West
    load = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                load += roll_west([row, col])
    cycle_outcome.append(load)
    #South
    load = 0
    for row in range(len(g) - 1, -1, -1):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                load += roll_south([row, col])
    cycle_outcome.append(load)
    # East
    load = 0
    for row in range(len(g)):
        for col in range(len(g[0]) - 1, -1, -1):
            if g[row][col] == "O":
                load += roll_east([row, col])
    cycle_outcome.append(load)
    return(cycle_outcome)


old_cycle_outcomes = []
cycle_num = 0
while cycle_num < cycles:
    cycle_num += 1
    cycle_outcome = cycle()
    old_cycle_outcomes.append(cycle_outcome)
    if len(old_cycle_outcomes) > 40:
        for i in range(2,1000):
            if old_cycle_outcomes[-i:] == old_cycle_outcomes[-2 * i:-i]:
                cycle_num += (cycles - cycle_num) // i * i
                print(cycle_num)
print(cycle_outcome)
load = 0
for row in range(len(g)):
    for col in range(len(g[0])):
        if g[row][col] == "O":
            load += len(g) - row
print(load)


