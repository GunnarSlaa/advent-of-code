import copy


def getNeighbours(cell):
    neighbourList = []
    neighbourList.append((cell[0] + 1, cell[1], cell[2]))
    neighbourList.append((cell[0] - 1, cell[1], cell[2]))
    neighbourList.append((cell[0], cell[1] + 1, cell[2]))
    neighbourList.append((cell[0], cell[1] - 1, cell[2]))
    neighbourList.append((cell[0], cell[1], cell[2] + 1))
    neighbourList.append((cell[0], cell[1], cell[2] - 1))
    return [nb for nb in neighbourList if max(nb) <= maxXYZ + 1 and min(nb) >= -1]

def checkReachable():
    queue = [(0,0,0)]
    openSet = {queue[0]}
    while len(queue) > 0:
        cell = queue.pop()
        neighbours = [nb for nb in getNeighbours(cell) if nb not in openSet]
        neighbours = [nb for nb in neighbours if nb not in grid]
        queue += neighbours
        openSet = openSet.union(set(neighbours))
    return openSet

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

maxXYZ = max(maxX, maxY, maxZ)
reachable = checkReachable()
print(len(reachable))
print(len(grid))

for x in range(maxX):
    for y in range(maxY):
        for z in range(maxZ):
            start = (x, y, z)
            if (x, y, z) not in reachable and (x, y, z) not in grid:
                grid[start] = 2

print(len(grid))


total = 0

for cell in grid.keys():
    if grid[cell] != 1: continue
    for neighhour in getNeighbours(cell):
        if neighhour not in grid:
            total += 1

print(total)