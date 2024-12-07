from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

result = 0

for line in lines:
    test_value = int(line.split(":")[0])
    values = [int(_) for _ in line.split(":")[1].split()]
    outcomes = [values[0]]
    for value in values[1:]:
        outcomes = [outcome + value for outcome in outcomes] + [outcome * value for outcome in outcomes] + [int(str(outcome) + str(value)) for outcome in outcomes]
    if test_value in outcomes:
        result += test_value

print(result)