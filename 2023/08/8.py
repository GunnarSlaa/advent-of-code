with open("input", "r") as file:
    lines = file.read().strip().split("\n")

lr = list(lines[0])

instructions = {}
for line in lines[2:]:
    instructions[line.split()[0]] = (line[7:10], line[12:15])

at = "AAA"
total = 0
while at != "ZZZ":
    look = total % len(lr)
    if lr[look] == "L":
        at = instructions[at][0]
    else:
        at = instructions[at][1]
    total += 1
print(total)