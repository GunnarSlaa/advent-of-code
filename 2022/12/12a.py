with open("input_test.txt", "r") as f:
    rows = f.read().split("\n")

start = (0,0)
end = (0,0)
gridDict = {}
for row in range(len(rows)):
    for col in range(len(rows[0])):
        if rows[row][col] == "S":
            start = (row, col)
        elif rows[row][col] == "E":
            end = (row, col)
        gridDict[(row,col)] = rows[row][col]

def isNeighbour(cell1, cell2):
    if not cell2 in gridDict: return False
    if gridDict[cell2] == "E" and gridDict[cell1] == "z": return True
    elif gridDict[cell2] == "E": return False
    if gridDict[cell1] == "S" and gridDict[cell2] == "a": return True
    if ord(gridDict[cell2]) <= ord(gridDict[cell1]) + 1:
        return True
    return False


def getNeighbours(cell):
    neighbourList = []
    if isNeighbour(cell, (cell[0] + 1, cell[1])):
        neighbourList.append((cell[0] + 1, cell[1]))
    if isNeighbour(cell, (cell[0] - 1, cell[1])):
        neighbourList.append((cell[0] - 1, cell[1]))
    if isNeighbour(cell, (cell[0], cell[1] + 1)):
        neighbourList.append((cell[0], cell[1] + 1))
    if isNeighbour(cell, (cell[0], cell[1] - 1)):
        neighbourList.append((cell[0], cell[1] - 1))
    return neighbourList

def gScore(cell):
    if cell in gScoreDict:
        return gScoreDict[cell]
    else:
        return 1_000_000


def fScore(cell):
    if cell in fScoreDict:
        return fScoreDict[cell]
    else:
        return 1_000_000


def hScore(cell):
    return abs(cell[0] - end[0]) + abs(cell[1] - end[1])


def reconstruct_path(current):
    path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        path.append(current)
    return path


openSet = [start]
cameFrom = {}
gScoreDict = {start: 0}
fScoreDict = {start: hScore(start)}
print(fScoreDict)
print(start, end)
while len(openSet) > 0:
    min = 10000
    for cell in openSet:
        if fScore(cell) < min:
            min = fScore(cell)
            current = cell
    if current == end:
        path = reconstruct_path(current)
        print(path)
        print(len(path))
        break
    print(current)
    openSet.remove(current)
    for neighbour in getNeighbours(current):
        tentative = gScoreDict[current] + 1
        if tentative < gScore(neighbour):
            cameFrom[neighbour] = current
            gScoreDict[neighbour] = tentative
            fScoreDict[neighbour] = tentative + hScore(neighbour)
            if neighbour not in openSet:
                openSet.append(neighbour)


print(getNeighbours((2, 0)))
