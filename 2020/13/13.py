from grid_utils import *
import math

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

time = int(lines[0])
busses = [int(c) for c in lines[1].split(",") if c != "x"]
mini = 10000
for bus in busses:
    if bus - (time % bus) < mini:
        mini = bus - (time % bus)
        best_bus = bus

print(best_bus * mini)