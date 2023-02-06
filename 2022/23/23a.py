with open("input", "r") as f:
    lines = f.read().split("\n")

def canMove(pos, direction):
    if direction == 0:
        if (pos[0], pos[1] - 1) not in elves and (pos[0] - 1, pos[1] - 1) not in elves and (pos[0] + 1, pos[1] - 1) not in elves:
            return (pos[0], pos[1] - 1)
        else:
            return None
    if direction == 1:
        if (pos[0] + 1, pos[1]) not in elves and (pos[0] + 1, pos[1] - 1) not in elves and (pos[0] + 1, pos[1] + 1) not in elves:
            return (pos[0] + 1, pos[1])
        else:
            return None
    if direction == 2:
        if (pos[0], pos[1] + 1) not in elves and (pos[0] - 1, pos[1] + 1) not in elves and (pos[0] + 1, pos[1] + 1) not in elves:
            return (pos[0], pos[1] + 1)
        else:
            return None
    if direction == 3:
        if (pos[0] - 1, pos[1]) not in elves and (pos[0] - 1, pos[1] - 1) not in elves and (pos[0] - 1, pos[1] + 1) not in elves:
            return (pos[0] - 1, pos[1])
        else:
            return None

def emptyAround(pos):
    return canMove(pos, 0) and canMove(pos, 1) and canMove(pos, 2) and canMove(pos, 3)

elves = []

for y, row in enumerate(lines):
    for x, col in enumerate(row):
        if col == "#": elves.append((x, y))

moveList = [0,2,3,1]
for _ in range(10):
    moveDict = {}
    blocked = []
    for elf in elves:
        move = None
        for dir in moveList:
            move = canMove(elf, dir)
            if move: break
        if emptyAround(elf): move = None
        if move:
            if move in blocked or move in moveDict.values():
                moveDict = {key:val for key, val in moveDict.items() if val != move}
                blocked.append(move)
            else:
                moveDict[elf] = move
    for elf, move in moveDict.items():
        elves.remove(elf)
        elves.append(move)
    moveList = moveList[1:] + [moveList[0]]
    print(moveList)
    print(len(elves))

print(elves)
max0 = min(tup[1] for tup in elves)
max1 = max(tup[0] for tup in elves)
max2 = max(tup[1] for tup in elves)
max3 = min(tup[0] for tup in elves)
for col in range(max0, max2 + 1):
    rowPrint = ""
    for row in range(max3, max1 + 1):
        if (row, col) in elves:
            rowPrint += "#"
        else:
            rowPrint += "."
    print(rowPrint)
print((max2 + 1 - max0) * (max1 + 1 - max3) - len(elves))