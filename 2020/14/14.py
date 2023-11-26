from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

mem = {}
for line in lines:
    if line.split()[0] == "mask":
        mask = list(line.split()[2])
    else:
        position = line.split()[0][4:-1]
        value = [0] * len(mask)
        num = list(bin(int(line.split()[2])))[2:]
        for i in range(1, len(num) + 1):
            value[-i] = int(num[-i])
        result = [int(mask[i]) if mask[i] != "X" else value[i] for i in range(len(mask))]
        result = [str(c) for c in result]
        result = int("".join(result), 2)
        mem[position] = result
print(sum([v for v in mem.values()]))


