def sandDrop(pos):
    for newPos in [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]:
        if newPos not in grid:
            return newPos
    return None

def newSand():
    pos = (500, 0)
    while True:
        #print(pos)
        newPos = sandDrop(pos)
        if newPos == None:
            grid[pos] = 2
            return pos != (500,0)
        pos = newPos


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

grid = {}
maxDepth = 0

for line in lines:
    pairs = [pair.split(",") for pair in line.split(" -> ")]
    pairs = [[eval(i) for i in pair] for pair in pairs]
    grid[tuple(pairs[0])] = 1
    maxDepth = max(maxDepth, pairs[0][1])
    for i in range(len(pairs) - 1):
        maxDepth = max(maxDepth, pairs[i + 1][1])
        grid[tuple(pairs[i + 1])] = 1
        if pairs[i][0] == pairs[i + 1][0]:
            mini = min(pairs[i][1], pairs[i + 1][1])
            maxi = max(pairs[i][1], pairs[i + 1][1])
            for row in range(mini, maxi):
                #print(row)
                grid[(pairs[i][0], row + 1)] = 1
        elif pairs[i][1] == pairs[i + 1][1]:
            mini = min(pairs[i][0], pairs[i + 1][0])
            maxi = max(pairs[i][0], pairs[i + 1][0])
            for col in range(mini, maxi):
                grid[(col, pairs[i][1])] = 1
for i in range(1000):
    grid[(i, maxDepth + 2)] = 1

numRock = len(grid)
print(maxDepth)
while newSand():
    continue
numSand = len(grid) - numRock
print(numRock, numSand)
# #27606 too low
# gridPrint = [["." for row in range(maxDepth + 2)] for col in range(300, 700)]
# print(len(gridPrint), len(gridPrint[0]))
#
# for pos in grid.keys():
#     print(pos)
#     print(pos[0], len(gridPrint))
#     print(pos[1], len(gridPrint[0]))
#     print(gridPrint[pos[0] - 300][pos[1]])
#     gridPrint[pos[0] - 300][pos[1]] = str(grid[pos])
#
# gridPrint = ["".join(row) for row in gridPrint]
# print("\n".join(gridPrint))

