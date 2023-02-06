file = open("Input4.txt", "r")
total = 0

for line in file:
    line = line.strip()
    elf1 = line.split(",")[0].split("-")
    elf2 = line.split(",")[1].split("-")
    elf1 = [int(x) for x in elf1]
    elf2 = [int(x) for x in elf2]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
        total += 1
        print(elf1, elf2)
print(total)