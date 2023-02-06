import time


def calcDist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

class Sensor:
    location : tuple
    distance: int

    def __init__(self, locX, locY, beaconX, beaconY):
        self.location = (locX, locY)
        self.distance = calcDist(self.location, (beaconX, beaconY))

    def __repr__(self):
        return str(self.location) + str(self.beacon) + str(self.distance)

    def blockCol(self, col):
        colDist = abs(self.location[0] - col)
        if colDist > self.distance: return None
        return (self.location[1] - self.distance + colDist, self.location[1] + self.distance - colDist)

st = time.time()

sensors = []
blockedCols = []
nonBlockedCol = 0
nonBlockedRow = 0

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
for line in lines:
    locX = line.split(" ")[2].split("=")[1].split(",")[0]
    locY = line.split(" ")[3].split("=")[1].split(":")[0]
    beaconX = line.split(" ")[8].split("=")[1].split(",")[0]
    beaconY = line.split(" ")[9].split("=")[1]
    newSensor = Sensor(int(locX), int(locY), int(beaconX), int(beaconY))
    sensors.append(newSensor)



def checkColBlocked(blocks):
    global nonBlockedRow
    blocks.sort()
    left = 0
    right = 4_000_000
    minOverlap = 4_000_000
    for i in range(len(blocks) - 1):
        if blocks[i][1] > right:
            return min(minOverlap, blocks[i][1] - right)
        left = max(blocks[i][1], left)
        if left + 1 < blocks[i + 1][0]:
            nonBlockedRow = blocks[i][1] + 1
            return "False"
        minOverlap = min(minOverlap, left - blocks[i + 1][0])
    return minOverlap

col = 0
countCalls = 0
while col < 4_000_001:
    blocksInCol = []
    for sensor in sensors:
        block = sensor.blockCol(col)
        if block: blocksInCol.append(block)
    countCalls += 1
    result = checkColBlocked(blocksInCol)
    if result == "False":
        nonBlockedCol = col
        break
    else: col += result // 2
    col += 1

print(nonBlockedCol, nonBlockedRow)
print(nonBlockedCol * 4_000_000 + nonBlockedRow)
print(countCalls)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')