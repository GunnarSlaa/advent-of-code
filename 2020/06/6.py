import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

total1 = 0
total2 = 0
for line in lines:
    group = line.replace("\n", "")
    people = line.split("\n")
    line_set = set([c for c in group])
    total1 += len(line_set)
    for q in line_set:
        if all(q in person for person in people):
            total2 += 1

print(total1)
print(total2)
