with open("input", "r") as file:
    lines = file.read().strip().split("\n")

def is_safe(values):
    for i in range(len(values)):
        new_values = values[:i]  + values[i+1:]
        diffs = [new_values[i] - new_values[i - 1] for i in range(1, len(new_values))]
        if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]):
            return True
    return False

result = 0
for line in lines:
    values = [int(i) for i in line.split()]
    if is_safe(values):
        result += 1

print(result)
