def isVisible(x, y):
    height = lines[y][x]
    return isVisible1(x, y, height) or isVisible2(x, y, height) or isVisible3(x, y, height) or isVisible4(x, y, height)


def isVisible1(x, y, height):
    if x == 0: return True
    for i in range(x):
        if lines[y][i] >= height: return False
    return True


def isVisible2(x, y, height):
    if y == 0: return True
    for j in range(y):
        if lines[j][x] >= height: return False
    return True


def isVisible3(x, y, height):
    if y == len(lines) - 1: return True
    for k in range(y + 1, len(lines)):
        #print(k)
        if lines[k][x] >= height: return False
    return True


def isVisible4(x, y, height):
    if x == len(lines[0]) - 1: return True
    for l in range(x + 1, len(lines[0])):
        if lines[y][l] >= height: return False
    return True


with open("Input8.txt", "r") as f:
    lines = f.read().split("\n")
trees = 0
print(len(lines))
for yp in range(len(lines)):
    for xp in range(len(lines[0])):
        if isVisible(int(xp), int(yp)):
            trees += 1
print(trees)