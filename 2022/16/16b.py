import copy
import time


class Valve:
    flowRate: int
    routes: dict
    fullRoutes: dict
    name: str

    def __init__(self, name, flowRate, tunnels):
        self.flowRate = int(flowRate)
        self.name = name
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

    def findFullRoutes(self, valveDict):
        dists = {}
        prev = {}
        Q = []
        for dest in valveDict.values():
            dists[dest.name] = 1000
            prev[dest.name] = None
            Q.append(dest.name)
        dists[self.name] = 0
        while len(Q) > 0:
            minDist = 10000
            u = None
            for x in Q:
                if dists[x] < minDist:
                    minDist = dists[x]
                    u = x
            Q.remove(u)
            for neighbour in [_ for _ in valveDict[u].routes.keys() if _ in Q]:
                alt = dists[u] + valveDict[u].routes[neighbour]
                if alt < dists[neighbour]:
                    dists[neighbour] = alt
                    prev[neighbour] = u
        self.fullRoutes = dists
        self.fullRoutes.pop(self.name)
        if "AA" in self.fullRoutes.keys(): self.fullRoutes.pop("AA")
        for key in self.fullRoutes.keys():
            self.fullRoutes[key] += 1

    def __repr__(self):
        return str(self.name) + ", " + str(self.flowRate) + ", " + str(self.routes)


class Path:
    currentLocation1: str
    currentLocation2: str
    openedValves: list
    score: int
    length1: int
    length2: int

    def __init__(self):
        self.currentLocation1 = "AA"
        self.currentLocation2 = "AA"
        self.openedValves = []
        self.score = 0
        self.length1 = 0
        self.length2 = 0

    def move(self, moveTo, number = False):
        if self.length1 <= self.length2 and not number:
            valve = valveDict[self.currentLocation1]
            self.length1 += valve.fullRoutes[moveTo]
            self.currentLocation1 = moveTo
            if self.length1 < 26: self.score += (26 - self.length1) * valveDict[self.currentLocation1].flowRate
        else:
            valve = valveDict[self.currentLocation2]
            self.length2 += valve.fullRoutes[moveTo]
            self.currentLocation2 = moveTo
            if self.length2 < 26: self.score += (26 - self.length2) * valveDict[self.currentLocation2].flowRate
        self.openedValves.append(moveTo)

        if min(valveDict[self.currentLocation1].routes.values()) > (26 - self.length1):
            self.length1 = 26
        if min(valveDict[self.currentLocation2].routes.values()) > (26 - self.length2):
            self.length2 = 26

        if len(self.openedValves) == len(valveDict) - 1:
            self.length1 = 26
            self.length2 = 26

        if ((52 - min(self.length2, 26) - min(self.length1, 26) - 4) * (maxFlow + maxFlow2)) + self.score < maxScore:
            #print("kansloos")
            self.length1 = 26
            self.length2 = 26

    def getNeighbours(self):
        if self.length1 <= self.length2:
            neighbours = valveDict[self.currentLocation1].routes.keys()
            neighbours = [_ for _ in neighbours if valveDict[self.currentLocation1].routes[_] + self.length1 < 26]
        else:
            neighbours = valveDict[self.currentLocation2].routes.keys()
            neighbours = [_ for _ in neighbours if valveDict[self.currentLocation2].routes[_] + self.length2 < 26]
        neighbours = [_ for _ in neighbours if _ not in self.openedValves]
        return neighbours

st = time.time()

valveDict = {}
with open("input", "r") as f:
    lines = f.read().split("\n")
for line in lines:
    name = line.split()[1]
    flowRate = line.split()[4].split("=")[1].split(";")[0]
    tunnels = [x.split(",")[0] for x in line.split()[9:]]
    valveDict[name] = Valve(name, flowRate, tunnels)

toRemove = []
for valve in valveDict.values():
    if valve.flowRate == 0 and valve.name != "AA":
        valve.removeValve(valveDict)
        toRemove.append(valve.name)
for item in toRemove:
    valveDict.pop(item)

for valve in valveDict.values():
    valve.findFullRoutes(valveDict)

for valve in valveDict.values():
    valve.routes = valve.fullRoutes

for valve in valveDict.values():
    print(valve)

maxFlow = max([valve.flowRate for valve in valveDict.values()])
maxFlow2 = max([valve.flowRate for valve in valveDict.values() if valve.flowRate != maxFlow])
paths = [Path()]
maxScore = 0
while len(paths) > 0:
    path = paths.pop()
    neighbours = path.getNeighbours()
    for moveTo in neighbours:
        movePath = copy.deepcopy(path)
        movePath.move(moveTo)
        paths.append(movePath)
        if path.length1 == path.length2 and path.currentLocation1 != path.currentLocation2:
            movePath2 = copy.deepcopy(path)
            movePath2.move(moveTo, True)
            paths.append(movePath2)
    toRemove=[]
    for path in paths:
        if path.length1 >= 26 and path.length2 >= 26:
            toRemove.append(path)
            if path.score > maxScore:
                maxScore = path.score
                maxScorePath = path.openedValves
                print(maxScore)
                print(maxScorePath)
    for path in toRemove:
        paths.remove(path)
print(maxScore)
print(maxScorePath)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
print(maxFlow, maxFlow2)




