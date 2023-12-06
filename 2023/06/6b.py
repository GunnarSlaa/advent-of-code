with open("input", "r") as file:
    lines = file.read().strip().split("\n")

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))


hold_sec = 0
while (time - hold_sec) * hold_sec <= distance:
    hold_sec += 1
mini = hold_sec
while (time - hold_sec) * hold_sec > distance:
    hold_sec += 1
maxi = hold_sec - 1
print(maxi - mini + 1)