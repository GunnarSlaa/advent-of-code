import copy


class Valve:
    flowRate: int
    routes: dict
    fullRoutes: dict
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
        return str(self.name) + ", " + str(self.flowRate) + ", " + str(self.opened) + ", " + str(self.routes)


class Path:
    currentLocation: str
    openedValves: list
    score: int
    length: int

    def __init__(self):
        self.currentLocation = "AA"
        self.openedValves = []
        self.score = 0
        self.length = 0

    def move(self, moveTo):
        valve = valveDict[self.currentLocation]
        self.length += valve.fullRoutes[moveTo]
        self.currentLocation = moveTo
        self.openedValves.append(moveTo)
        if self.length < 30: self.score += (30 - self.length) * valveDict[self.currentLocation].flowRate
        if min(valveDict[self.currentLocation].routes.values()) > (30 - self.length):
            self.length = 30
        if len(self.openedValves) == len(valveDict) - 1:
            self.length = 30

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

paths = [Path()]
maxScore = 0
while len(paths) > 0:
    path = paths.pop()
    neighbours = valveDict[path.currentLocation].routes.keys()
    neighbours = [_ for _ in neighbours if _ not in path.openedValves]
    for moveTo in neighbours:
        movePath = copy.deepcopy(path)
        movePath.move(moveTo)
        paths.append(movePath)
    toRemove=[]
    for path in paths:
        #print(path.length)
        if path.length >= 30:
            toRemove.append(path)
            #print("SCORE " + path.score)
            if path.score > maxScore:
                maxScore = path.score
                maxScorePath = path.openedValves
    for path in toRemove:
        paths.remove(path)
print(maxScore)
print(maxScorePath)




