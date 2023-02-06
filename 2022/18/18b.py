def getNeighbours(cell):
    neighbourList = []
    neighbourList.append((cell[0] + 1, cell[1], cell[2]))
    neighbourList.append((cell[0] - 1, cell[1], cell[2]))
    neighbourList.append((cell[0], cell[1] + 1, cell[2]))
    neighbourList.append((cell[0], cell[1] - 1, cell[2]))
    neighbourList.append((cell[0], cell[1], cell[2] + 1))
    neighbourList.append((cell[0], cell[1], cell[2] - 1))
    return neighbourList


def gScore(cell, dict):
    if cell in dict:
        return dict[cell]
    else:
        return 1_000_000


def fScore(cell, dict):
    if cell in dict:
        return dict[cell]
    else:
        return 1_000_000


def hScore(cell):
    return abs(cell[0] - end[0]) + abs(cell[1] - end[1]) + abs(cell[2] - end[2])


def checkRoute(start):
    openSet = [start]
    cameFrom = {}
    gScoreDict = {start: 0}
    fScoreDict = {start: hScore(start)}
    while len(openSet) > 0:
        min = 10000
        for cell in openSet:
            if fScore(cell, fScoreDict) < min:
                min = fScore(cell, fScoreDict)
                current = cell
        if current == end:
            return True
        openSet.remove(current)
        for neighbour in [nb for nb in getNeighbours(current) if nb not in grid or grid[nb] != 1]:
            tentative = gScoreDict[current] + 1
            if tentative < gScore(neighbour, gScoreDict):
                cameFrom[neighbour] = current
                gScoreDict[neighbour] = tentative
                fScoreDict[neighbour] = tentative + hScore(neighbour)
                if neighbour not in openSet:
                    openSet.append(neighbour)
    return False

grid = {}


with open("input", "r") as f:
    lines = f.read().split("\n")

maxX = 0
maxY = 0
maxZ = 0

for line in lines:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    z = int(line.split(",")[2])
    maxX = max(x, maxX)
    maxY = max(y, maxY)
    maxZ = max(z, maxZ)
    grid[(x, y, z)] = 1

end = (0,0,0)


for x in range(maxX):
    print(x)
    for y in range(maxY):
        for z in range(maxZ):
            start = (x, y, z)
            if not checkRoute(start):
                grid[start] = 2



total = 0

for cell in grid.keys():
    if grid[cell] != 1: continue
    for neighhour in getNeighbours(cell):
        if neighhour not in grid:
            total += 1

print(total)