from grid_utils import *
import math

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

busses = [c for c in lines[1].split(",")]
timestamp = 0
bustimes = []
for bus in busses:
    if bus != "x":
        bustimes.append([timestamp % int(bus), int(bus)])
    timestamp += 1
beat = bustimes[0][1]
start = 0
for bus in bustimes[1:]:
    found = []
    i = 1
    while len(found) < 2:
        if ((start + i * beat) + bus[0]) % bus[1] == 0:
            found.append(start + i * beat)
        i += 1
    beat = found[1] - found[0]
    start = found[0]
print(found[0])