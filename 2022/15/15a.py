def calcDist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def isPossible(pos):
    if pos in beacons:
        print(pos)
        return True
    for sensor in sensors:
        if calcDist(pos, sensor.location) <= sensor.distance:
            return False
    return True

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


sensors = []
beacons = []

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
for line in lines:
    locX = line.split(" ")[2].split("=")[1].split(",")[0]
    locY = line.split(" ")[3].split("=")[1].split(":")[0]
    beaconX = line.split(" ")[8].split("=")[1].split(",")[0]
    beaconY = line.split(" ")[9].split("=")[1]
    sensors.append(Sensor(int(locX), int(locY), int(beaconX), int(beaconY)))
    beacons.append((int(beaconX), int(beaconY)))
minX = min([s.location[0] for s in sensors])
maxX = max([s.location[0] for s in sensors])
maxDist = max([s.distance for s in sensors])
posY = 2_000_000
count = 0
for posX in range(minX - maxDist, maxX + maxDist):
    if posX % 100_000 == 0: print(posX)
    if not isPossible((posX, posY)): count += 1
print(count)