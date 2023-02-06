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
    sets = f.read().split("\n\n")

total = 0

for i, set in enumerate(sets):
    left = eval(set.split()[0])
    right = eval(set.split()[1])
    if compare(left, right):
        total += i + 1

print(total)
#6484