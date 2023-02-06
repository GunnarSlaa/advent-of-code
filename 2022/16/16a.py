import copy


class Valve:
    flowRate: int
    routes: dict
    name: str
    opened: bool

    def __init__(self, name, flowRate, tunnels):
        self.flowRate = int(flowRate)
        self.name = name
        self.opened = False
        self.routes = {}
        for tunnel in tunnels:
            self.routes[tunnel] = 1

    def removeValve(self, valveDict):
        routesToUpdate = [route for route in self.routes.keys()]
        for route in routesToUpdate:
            valveDict[route].updateRoutes(self.name, self.routes)

    def updateRoutes(self, valve, theirRoutes):
        if valve not in self.routes: return
        distTo = self.routes[valve]
        for routeTo, dist in theirRoutes.items():
            if routeTo == self.name: continue
            if routeTo not in self.routes:
                self.routes[routeTo] = dist + distTo
            else: self.routes[routeTo] = min(self.routes[routeTo], dist + distTo)
        self.routes.pop(valve)

    def __repr__(self):
        return str(self.name) + ", " + str(self.flowRate) + ", " + str(self.opened) + ", " + str(self.routes)

class Path:
    currentLocation: str
    openedValves: list
    currentScore: int
    scorePerTurn: int
    length: int
    valveDict: dict

    def __init__(self, valveDict):
        self.currentLocation = "AA"
        self.openedValves = []
        self.currentScore = 0
        self.scorePerTurn = 0
        self.length = 0
        self.valveDict = valveDict

    def addLength(self, amount):
        self.length += amount
        self.currentScore += int(amount) * int(self.scorePerTurn)

    def openValve(self):
        self.openedValves.append(self.currentLocation)
        self.addLength(1)
        self.scorePerTurn += self.valveDict[self.currentLocation].flowRate
        self.checkDone()

    def move(self, moveTo):
        valve = self.valveDict[self.currentLocation]
        self.addLength(self.valveDict[self.currentLocation].routes[moveTo])
        if valve.flowRate == 0 or valve.opened:
            valve.removeValve(self.valveDict)
            self.valveDict.pop(valve.name)
        self.currentLocation = moveTo
        self.checkDone()

    def checkDone(self):
        if min(self.valveDict[self.currentLocation].routes.values()) > (30 - self.length):
            self.length = 30
            self.currentScore += (self.length - 30) * self.scorePerTurn

mainValveDict = {}
with open("input_test", "r") as f:
    lines = f.read().split("\n")
for line in lines:
    name = line.split()[1]
    flowRate = line.split()[4].split("=")[1].split(";")[0]
    tunnels = [x.split(",")[0] for x in line.split()[9:]]
    mainValveDict[name] = Valve(name, flowRate, tunnels)
    #print(name, flowRate, tunnels)

toRemove = []
for valve in mainValveDict.values():
    if valve.flowRate == 0 and valve.name != "AA":
        valve.removeValve(mainValveDict)
        toRemove.append(valve.name)
for item in toRemove:
    mainValveDict.pop(item)

# for valve in valveDict.values():
#     print(valve)

paths = [Path(mainValveDict)]
maxScore = 0
minAvgToGo = 30
pathsCompleted = 0
while len(paths) > 0:
    path = paths.pop()
    if path.currentLocation not in path.openedValves and path.currentLocation != "AA":
        #Opening valve an option
        openPath = copy.deepcopy(path)
        openPath.openValve()
        paths.append(openPath)
    for moveTo in path.valveDict[path.currentLocation].routes.keys():
        movePath = copy.deepcopy(path)
        movePath.move(moveTo)
        paths.append(movePath)
    #print("LEN: " + str(len(paths)))
    toRemove = []
    for path in paths:
        #print(path.length)
        if path.length >= 30:
            toRemove.append(path)
            maxScore = max(maxScore, path.currentScore)
    for path in toRemove:
        pathsCompleted += 1
        if pathsCompleted % 10_000 == 0:
            print(pathsCompleted)
        paths.remove(path)
    #print("LEN_AFTER: " + str(len(paths)))
    #print("TOTAL_TO_GO: " + str(sum([30 - path.length for path in paths])))
    avgToGo = sum([30 - path.length for path in paths]) // len(paths)
    if avgToGo < minAvgToGo:
        print(avgToGo)
        minAvgToGo = avgToGo
    #print("AVG_TO_GO: " + str(sum([30 - path.length for path in paths])// len(paths)))
print(maxScore)

