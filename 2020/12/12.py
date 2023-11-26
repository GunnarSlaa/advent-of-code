from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

direction = 1
pos = [0,0]
for line in lines:
    inst = line[0]
    amount = int(line[1:])
    if inst == "N" or inst == "F" and direction == 0:
        pos[0] += amount
    elif inst == "E" or inst == "F" and direction == 1:
        pos[1] += amount
    elif inst == "S" or inst == "F" and direction == 2:
        pos[0] -= amount
    elif inst == "W" or inst == "F" and direction == 3:
        pos[1] -= amount
    elif inst == "R":
        direction = (direction + (amount / 90)) % 4
    elif inst == "L":
        direction = (direction - (amount / 90)) % 4
        print(direction)

print(abs(pos[0]) + abs(pos[1]))