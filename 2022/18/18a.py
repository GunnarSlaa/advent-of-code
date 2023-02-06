def getNeighbours(cell):
    neighbourList = []
    neighbourList.append((cell[0] + 1, cell[1], cell[2]))
    neighbourList.append((cell[0] - 1, cell[1], cell[2]))
    neighbourList.append((cell[0], cell[1] + 1, cell[2]))
    neighbourList.append((cell[0], cell[1] - 1, cell[2]))
    neighbourList.append((cell[0], cell[1], cell[2] + 1))
    neighbourList.append((cell[0], cell[1], cell[2] - 1))
    return neighbourList

grid = []

with open("input", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    z = int(line.split(",")[2])
    grid.append((x, y, z))

total = 0

for cell in grid:
    for neighhour in getNeighbours(cell):
        if neighhour not in grid:
            total += 1

print(total)