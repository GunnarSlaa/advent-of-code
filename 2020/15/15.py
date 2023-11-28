from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

starting = [int(c) for c in lines[0].split(",")]
last = starting[-1]
last_spoken = {c: starting.index(c) + 1 for c in starting[:-1]}

for i in range(len(starting) + 1, 30000000 + 1):
    if last in last_spoken.keys():
        number = i - last_spoken[last] - 1
    else:
        number = 0
    last_spoken[last] = i - 1
    last = number
    if i == 2020:
        print(number)
print(number)
