with open("input.txt", "r") as f:
    lines = f.read().split("\n")

cycle = 1
x = 1
screen = [["." for _ in range(40)] for _ in range(6)]
row = 0


def addCycle():
    global cycle
    global row
    if cycle == 41:
        cycle = 1
        row += 1
        if row == 6: return
    print(row, cycle, x)
    if abs((cycle - 1) - x) < 2:
        screen[row][cycle - 1] = "#"
    cycle += 1


for line in lines:
    if row >= 6: break
    if line == "noop": addCycle()
    else:
        val = int(line.split()[1])
        addCycle()
        if row >= 6: break
        addCycle()
        x += val

for line in screen:
    print("".join(line))