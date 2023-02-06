import time


def calcDist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

class Sensor:
    location : tuple
    beacon : tuple
    distance: int

    def __init__(self, locX, locY, beaconX, beaconY):
        self.location = (locX, locY)
        self.beacon = (beaconX, beaconY)
        self.distance = calcDist(self.location, self.beacon)

    def __repr__(self):
        return str(self.location) + str(self.beacon) + str(self.distance)

    def blockCol(self, col):
        colDist = abs(self.location[0] - col)
        return (self.location[1] - self.distance + colDist, self.location[1] + self.distance - colDist)

    def blocking(self):
        blockList = set()
        for y in range(self.location[1] - self.distance, self.location[1] + self.distance):
            yDist = abs(self.location[1] - y)
            #print(y, yDist)
            #print(self.location[0] - self.distance + yDist, self.location[0] + self.distance - yDist)
            for x in range(self.location[0] - self.distance + yDist, self.location[0] + self.distance - yDist + 1):
                blockList.add((x, y))
        #print(len(blockList))
        return blockList

st = time.time()

sensors = []
blockedCols = []
nonBlockedCols = []

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
for line in lines:
    locX = line.split(" ")[2].split("=")[1].split(",")[0]
    locY = line.split(" ")[3].split("=")[1].split(":")[0]
    beaconX = line.split(" ")[8].split("=")[1].split(",")[0]
    beaconY = line.split(" ")[9].split("=")[1]
    newSensor = Sensor(int(locX), int(locY), int(beaconX), int(beaconY))
    sensors.append(newSensor)
    #print(len(sensors))

def checkInBlocks(blocks, point):
    for block in blocks:
        if point >= block[0] and point <= block[1]: return True
    return False

def checkColBlocked(blocks):
    left = 0
    right = 4_000_000
    #right = 20
    while(left < right):
        list = [block[1] + 1 for block in blocks if block[0] <= left and block[1] > left]
        if len(list) == 0:
            print("LEFT:" + str(left))
            return False
        left = max(list)
    return True

for col in range(4_000_001):
    if col % 100_000 == 0: print(col)
    blocksInCol = []
    for sensor in sensors:
        blocksInCol.append(sensor.blockCol(col))
    if checkColBlocked(blocksInCol):
        blockedCols.append(col)
    else:
        #print(col)
        nonBlockedCols.append(col)

#print(len(blockedCols))
#print(len(nonBlockedCols))
print(nonBlockedCols)
#col: 3267801
#row?: 2703981

def isPossible(pos):
    for sensor in sensors:
        if calcDist(pos, sensor.location) <= sensor.distance:
            return False
    return True

print(isPossible((3267801, 2703981)))
print(3267801 * 4_000_000 + 2703981)
print(isPossible((2703981, 3267801)))

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')