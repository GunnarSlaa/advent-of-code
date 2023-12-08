import math
from functools import reduce

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

lr = list(lines[0])

instructions = {}
for line in lines[2:]:
    instructions[line.split()[0]] = (line[7:10], line[12:15])

at = [node for node in instructions.keys() if node[2] == "A"]
totals = []
for node in at:
    total = 0
    hits = []
    while len(hits) < 2:
        if node[2] == "Z":
            hits.append(total)
        look = total % len(lr)
        if lr[look] == "L":
            node = instructions[node][0]
        else:
            node = instructions[node][1]
        total += 1
    totals.append(hits)

#Check if the cycle repeats
print([t[1] / t[0] for t in totals])
print(reduce(math.lcm, [t[0] for t in totals]))