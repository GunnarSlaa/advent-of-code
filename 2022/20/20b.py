with open("input", "r") as f:
    lines = f.read().split("\n")

list = [(int(line) * 811589153, i) for i, line in enumerate(lines)]

length = len(list)
for _ in range(10):
    for i in range(length):
        for j, tup in enumerate(list):
            if tup[1] == i:
                break
        list.remove(tup)
        index = (j + tup[0]) % (length - 1)
        list.insert(index, tup)
for j, tup in enumerate(list):
    if tup[0] == 0:
        break
print(sum([list[(j + x) % length][0] for x in (1000, 2000, 3000)]))