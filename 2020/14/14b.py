from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")


def dup(list):
    if not "X" in list: return [list]
    first_X = list.index("X")
    with_0 = list[:first_X] + ["0"] + list[first_X + 1:]
    with_1 = list[:first_X] + ["1"] + list[first_X + 1:]
    return dup(with_0) + dup(with_1)

mem = {}
for line in lines:
    if line.split()[0] == "mask":
        mask = list(line.split()[2])
    else:
        position = list(bin(int(line.split()[0][4:-1]))[2:])
        value = [0] * len(mask)
        num = int(line.split()[2])
        for i in range(1, len(position) + 1):
            value[-i] = int(position[-i])
        result = [str(mask[i]) if mask[i] != "0" else str(value[i]) for i in range(len(mask))]
        positions = dup(result)
        positions = [int("".join(c), 2) for c in positions]
        for position in positions:
            mem[position] = num
print(sum([v for v in mem.values()]))



