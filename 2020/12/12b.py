from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

pos = [1,10]
ship_pos = [0,0]
for line in lines:
    print(pos)
    print(ship_pos)
    print(line)

    inst = line[0]
    amount = int(line[1:])
    if inst == "N":
        pos[0] += amount
    elif inst == "E":
        pos[1] += amount
    elif inst == "S":
        pos[0] -= amount
    elif inst == "W":
        pos[1] -= amount
    elif inst == "R":
        for i in range(int(amount/90)):
            pos = [-pos[1], pos[0]]
    elif inst == "L":
        for i in range(int(amount/90)):
            pos = [pos[1], -pos[0]]
    elif inst == "F":
        ship_pos = [ship_pos[0] + amount * pos[0], ship_pos[1] + amount * pos[1]]

print(abs(ship_pos[0]) + abs(ship_pos[1]))