import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

lst = []
for line in lines:
    col = line[-3:]
    col = int(col.replace("L", "0").replace("R", "1"), 2)
    row = line[:-3]
    row = int(row.replace("F", "0").replace("B", "1"), 2)
    lst.append(8*row + col)

print(max(lst))

lst.sort()
for i in range(1, len(lst) - 1):
    if lst[i] != lst[i-1] + 1:
        print(lst[i])
    if lst[i] != lst[i+1] - 1:
        print(lst[i])
