import itertools
import re

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
for line in lines:
    digits = re.findall(r'\d', line)
    total += int("".join([digits[0], digits[-1]]))

print(total)