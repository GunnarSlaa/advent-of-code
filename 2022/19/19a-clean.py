import time
import copy

class BluePrint:
    oreCostOre: int
    clayCostOre: int
    obsidianCostOre: int
    obsidianCostClay: int
    geodeCostOre: int
    geodeCostObsidian: int

    def __init__(self, oreCostOre, clayCostOre, obsidianCostOre, obsidianCostClay, geodeCostOre, geodeCostObsidian):
        self.oreCostOre = int(oreCostOre)
        self.clayCostOre = int(clayCostOre)
        self.obsidianCostOre = int(obsidianCostOre)
        self.obsidianCostClay = int(obsidianCostClay)
        self.geodeCostOre = int(geodeCostOre)
        self.geodeCostObsidian = int(geodeCostObsidian)

    def __repr__(self):
        return str([self.oreCostOre, self.clayCostOre, self.obsidianCostOre, self.obsidianCostClay, self.geodeCostOre, self.geodeCostObsidian])

class Path:
    length: int
    robots: list
    resources: list
    bluePrint: BluePrint
    costs: list
    producing: int
    isProducing: bool
    produced: str
    maxOre: int
    maxClay: int
    maxObsidian: int

    def __init__(self, bluePrint):
        self.robots = [1,0,0,0]
        self.resources = [0,0,0,0]
        self.bluePrint = bluePrint
        self.costs = []
        self.costs.append([bluePrint.oreCostOre, 0, 0, 0])
        self.costs.append([bluePrint.clayCostOre, 0, 0, 0])
        self.costs.append([bluePrint.obsidianCostOre, bluePrint.obsidianCostClay, 0, 0])
        self.costs.append([bluePrint.geodeCostOre, 0, bluePrint.geodeCostObsidian, 0])
        self.length = 0
        self.isProducing = False
        self.produced = ""
        self.maxOre = max(bluePrint.oreCostOre, bluePrint.clayCostOre, bluePrint.obsidianCostOre, bluePrint.geodeCostOre)
        self.maxClay = bluePrint.obsidianCostClay
        self.maxObsidian = bluePrint.geodeCostObsidian

    def collect(self):
        global skipped
        self.resources = [self.resources[i] + self.robots[i] for i in range(len(self.robots))]
        if self.isProducing:
            self.robots[self.producing] += 1
            self.isProducing = False
            self.produced += str(self.producing)
        else:
            self.produced += "-"
        self.length += 1
        if self.length == 24: return
        scenario = self.robots + self.resources
        scenario = tuple(scenario)
        #Skip when we can't make it anymore
        timeToGo = 24 - self.length
        maxReachable = self.resources[3] + self.robots[3] * timeToGo + ((timeToGo * (timeToGo - 1)) / 2)
        if maxReachable < maxScore:
            skipped[2] += 1
            self.length = 24
            return
        #Skip when too far behind
        if self.resources[3] + 2 < maxPerPhase[self.length]:
            skipped[3] += 1
            self.length = 24
            return
        elif self.resources[3] > maxPerPhase[self.length]:
            maxPerPhase[self.length] = self.resources[3]
        #Skip when this has been reached sooner
        if scenario in scenarios.keys():
            if scenarios[scenario] <= self.length:
                skipped[0] += 1
                self.length = 24
                return
        scenarios[scenario] = self.length

    def canProduce(self):
        result = [all([self.resources[i] >= self.costs[j][i] for i in range(4)]) for j in range(4)]
        return [i for i in range(4) if result[i]]


    def produce(self, robot):
        self.resources = [self.resources[i] - self.costs[robot][i] for i in range(len(self.robots))]
        self.producing = robot
        self.isProducing = True


st = time.time()

bluePrints = []

with open("input", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    words = line.split()
    bluePrints.append(BluePrint(words[6], words[12], words[18], words[21], words[27], words[30]))

def cleanOptions(options, path):
    if path.length == 23: return ["-"]
    if 3 in options: return [3]
    #elif 2 in options: return [2]
    if len(options) <= len([robot for robot in path.robots if robot != 0]):
        options.append("-")
    if path.length == 22 or path.maxObsidian <= path.robots[2]:
        if 2 in options:
            options.remove(2)
            skipped[1] += 1
    if path.length == 21 or path.maxClay <= path.robots[1] or 2 in options:
        if 1 in options:
            options.remove(1)
            skipped[1] += 1
    if path.maxOre <= path.robots[0] or 2 in options:
        if 0 in options:
            options.remove(0)
            skipped[1] += 1
    if options == []:
        options = ["-"]
        print("empty")
    return options

totalScore = 0
for i, bluePrint in enumerate(bluePrints):
    paths = [Path(bluePrint)]
    maxPerPhase = [0 for i in range(24)]
    skipped = [0,0,0,0]
    maxScore = 0
    pathsCompleted = 0
    scenarios = {}
    ot = time.time()
    while len(paths) > 0:
        path = paths.pop()
        options = cleanOptions(path.canProduce(), path)
        for robotToProduce in options:
            if robotToProduce == "-":
                nothingPath = copy.deepcopy(path)
                nothingPath.collect()
                paths.append(nothingPath)
            else:
                newPath = copy.deepcopy(path)
                newPath.produce(robotToProduce)
                newPath.collect()
                paths.append(newPath)
        toRemove = []
        for path in paths:
            if path.length >= 24:
                toRemove.append(path)
                if path.resources[3] > maxScore:
                    maxScore = max(maxScore, path.resources[3])
                    maxRobots = path.robots
                    maxResources = path.resources
                    maxProduced = path.produced
        for path in toRemove:
            pathsCompleted += 1
            paths.remove(path)
    totalScore += maxScore * (i + 1)
    print(i + 1, maxScore, totalScore)
    print(skipped)
    et = time.time()
    print(et-ot)
    ot = et
    print(maxPerPhase)
print(totalScore)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
#2, 2, 2, 2, 52, 76, 118, 118, 118, 148, 148, 148
#2, 0, 0, 0, 10, 4, 7, 0, 0, 4, 0, 0, 8, 7, 1, 2, 1, 1, 1, 2, 2, 2, 5, 0, 0, 0, 2, 6, 1,