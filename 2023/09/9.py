with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
total2 = 0
for line in lines:
    line = [int(c) for c in line.split()]
    lasts = [line[-1]]
    firsts = [line[0]]
    while any([c != 0 for c in line]):
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        lasts.append(line[-1])
        firsts.append(line[0])
    total += sum(lasts)
    before = 0
    for i in range(len(firsts) -2, -1, -1):
        before = firsts[i] - before
    total2 += before

print(total)
print(total2)
