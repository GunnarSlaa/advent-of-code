import re

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

result = 0
for line in lines:
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for match in matches:
        part1 = match.split("(")[1].split(",")[0]
        part2 = match.split(",")[1].split(")")[0]
        result += int(part1) * int(part2)

print(result)
