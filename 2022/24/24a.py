import copy

with open("input", "r") as f:
    lines = f.read().split("\n")

blizzards = []

def moveBlizzard(blizzard):
    if blizzard[1] == 0:
        if blizzard[0][1] == 1:
            blizzard[0] = (blizzard[0][0], maxY)
        else:
            blizzard[0] = (blizzard[0][0], blizzard[0][1] - 1)
    if blizzard[1] == 1:
        if blizzard[0][0] == maxX:
            blizzard[0] = (1, blizzard[0][1])
        else:
            blizzard[0] = (blizzard[0][0] + 1, blizzard[0][1])
    if blizzard[1] == 2:
        if blizzard[0][1] == maxY:
            blizzard[0] = (blizzard[0][0], 1)
        else:
            blizzard[0] = (blizzard[0][0], blizzard[0][1] + 1)
    if blizzard[1] == 3:
        if blizzard[0][0] == 1:
            blizzard[0] = (maxX, blizzard[0][1])
        else:
            blizzard[0] = (blizzard[0][0] - 1, blizzard[0][1])

def possDests(pos):
    neighbours = [pos, (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    #Can't go into blizzard
    neighbours = [nb for nb in neighbours if nb not in [l[0] for l in blizzards]]
    #Can't go into wall
    neighbours = [nb for nb in neighbours if (0 < nb[0] <= maxX and 0 < nb[1] <= maxY) or nb == (1,0) or nb == (maxX, maxY + 1)]
    return neighbours

for y, row in enumerate(lines):
    for x, col in enumerate(row):
        if col == "^":
            blizzards.append([(x, y), 0])
        elif col == ">":
            blizzards.append([(x, y), 1])
        elif col == "v":
            blizzards.append([(x, y), 2])
        elif col == "<":
            blizzards.append([(x, y), 3])

maxY = len(lines) - 2
maxX = len(lines[0]) - 2
print(maxX, maxY)
pathsDone = 0

def findPath(start, end):
    global time
    positions = set()
    positions.add(start)
    done = False

    while not done:
        newPositions = set()
        for blizzard in blizzards:
            moveBlizzard(blizzard)
        for poss in positions:
            # print(poss)
            for p in possDests(poss):
                newPositions.add(p)
            if poss == end:
                done = True
        positions = copy.deepcopy(newPositions)
        if time % 10 == 0:
            print("---", time, pathsDone, "/ 3")
            print(len(positions))
        time += 1

time = 0
findPath((1, 0), (maxX, maxY + 1))
pathsDone += 1
findPath((maxX, maxY + 1), (1, 0))
pathsDone += 1
findPath((1, 0), (maxX, maxY + 1))
print(time - 1)
print((maxX, maxY + 1))
