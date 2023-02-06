def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return "DONE"
        else: return right == left
    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return True
        if len(left) == 0 and len(right) > 0:
            return "DONE"
        elif len(right) == 0:
            return False
        result = compare(left[0], right[0])
        if result != True:
            return result
        else:
            return compare(left[1:], right[1:])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


with open("input.txt", "r") as f:
    lines = f.read().split("\n")
lines = [eval(line) for line in lines if line != ""]
lines.append([[6]])
lines.append([[2]])

for stopAt in reversed(range(len(lines))):
    for pos in range(stopAt):
        if not compare(lines[pos], lines[pos + 1]):
            lines[pos], lines[pos + 1] = lines[pos + 1], lines[pos]
pos2 = lines.index([[2]]) + 1
pos6 = lines.index([[6]]) + 1
print(pos2, pos6, pos2 * pos6)
#19305