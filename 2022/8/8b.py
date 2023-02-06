def scenicScore(x, y):
    height = lines[y][x]
    return scenicScore1(x, y, height) * scenicScore2(x, y, height) * scenicScore3(x, y, height) * scenicScore4(x, y, height)


def scenicScore1(x, y, height):
    if x == 0: return 0
    score = 0
    for i in reversed(range(x)):
        score += 1
        if lines[y][i] >= height: break
    return score


def scenicScore2(x, y, height):
    if y == 0: return 0
    score = 0
    for j in reversed(range(y)):
        score += 1
        if lines[j][x] >= height: break
    return score


def scenicScore3(x, y, height):
    if y == len(lines) - 1: return 0
    score = 0
    for k in range(y + 1, len(lines)):
        score += 1
        if lines[k][x] >= height: break
    return score


def scenicScore4(x, y, height):
    if x == len(lines[0]) - 1: return 0
    score = 0
    for l in range(x + 1, len(lines[0])):
        score += 1
        if lines[y][l] >= height: break
    return score


with open("Input8.txt", "r") as f:
    lines = f.read().split("\n")
maxScore = 0
print(len(lines))
for yp in range(len(lines)):
    for xp in range(len(lines[0])):
        if scenicScore(int(xp), int(yp)) > maxScore:
            maxScore = scenicScore(int(xp), int(yp))
print(maxScore)
