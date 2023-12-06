import numpy as np

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

times = [int(c) for c in lines[0].split()[1:]]
distances = [int(c) for c in lines[1].split()[1:]]

lst = []
for time, distance in zip(times, distances):
    hold_sec = 0
    while (time - hold_sec) * hold_sec <= distance:
        hold_sec += 1
    mini = hold_sec
    while (time - hold_sec) * hold_sec > distance:
        hold_sec += 1
    maxi = hold_sec - 1
    lst.append(maxi - mini + 1)

print(np.prod(lst))