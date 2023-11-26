import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

for subset in itertools.combinations(lines, 2):
    if sum([int(i) for i in subset]) == 2020:
        print(int(subset[0]) * int(subset[1]))

for subset in itertools.combinations(lines, 3):
    if sum([int(i) for i in subset]) == 2020:
        print(int(subset[0]) * int(subset[1]) * int(subset[2]))
