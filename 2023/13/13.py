with open("input", "r") as file:
    blocks = file.read().strip().split("\n\n")


def check_mirror2(lines, i):
    to_check = min(len(lines) - i - 1, i + 1)
    diff = 0
    for c in range(to_check):
        diff += check_diff(lines[i - c - 0],lines[i + c + 1])
        if diff > 1:
            return False
    return True


def check_mirror1(lines, i):
    to_check = min(len(lines) - i - 1, i + 1)
    for c in range(to_check):
        if lines[i - c] != lines[i + c + 1]:
            return False
    return True


def check_diff(line1, line2):
    return len([i for i in range(len(line1)) if line1[i] != line2[i]])


answer1 = 0
answer2 = 0
for block in blocks:
    rows = block.split("\n")
    cols = ["".join([row[i] for row in rows]) for i in range(len(rows[0]))]
    for i in range(len(rows) - 1):
        if check_mirror1(rows, i):
            answer1 += 100 * (i + 1)
        elif check_mirror2(rows, i):
            answer2 += 100 * (i + 1)
    for i in range(len(cols) - 1):
        if check_mirror1(cols, i):
            answer1 += i + 1
        elif check_mirror2(cols, i):
            answer2 += i + 1

print(answer1)
print(answer2)


