import re

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

dontstrings = lines[0].split("don't()")
dostrings = [line.split("do()", 1)[1] for line in dontstrings if "do()" in line] + [dontstrings[0]]
dontstrings = [line.split("do()", 1)[0] for line in dontstrings[1:]]

result = 0
for string in dostrings:
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", string)
    for match in matches:
        part1 = match.split("(")[1].split(",")[0]
        part2 = match.split(",")[1].split(")")[0]
        result += int(part1) * int(part2)

print(result)
