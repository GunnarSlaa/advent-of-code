with open("input.txt", "r") as f:
    lines = f.read().split("\n")

cycle = 1
total = 0
x = 1
screen = ["." * 20 for _ in range(6)]


def addCycle(line):
    global cycle
    global total
    if (cycle + 20) % 40 == 0:
        total += x * cycle
        print(cycle, x)
        print(line)
    cycle += 1


for line in lines:
    if line == "noop": addCycle(line)
    else:
        val = int(line.split()[1])
        addCycle(line)
        addCycle(line)
        x += val

print(total)
for line in screen:
    print(line)