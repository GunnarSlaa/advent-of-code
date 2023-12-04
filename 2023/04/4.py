with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
copies = [1] * len(lines)

for i, line in enumerate(lines):
    winning = line.split(": ")[1].split(" | ")[0].split()
    mine = line.split(": ")[1].split(" | ")[1].split()
    matches = sum([c in winning for c in mine])
    if matches > 0:
        total += 2 ** (matches - 1)
        for j in range(matches):
            copies[i + j + 1] += copies[i]

print(total)
print(sum(copies))
