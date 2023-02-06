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
        scenario = self.robots + self.resources
        scenario = tuple(scenario)
        #Skip when we can't make it anymore
        timeToGo = 24 - self.length
        maxReachable = self.resources[3] + self.robots[3] * timeToGo + ((timeToGo * (timeToGo - 1)) / 2)
        if maxReachable < maxScore:
            skipped[2] += 1
            self.length = 24
            return
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

with open("input_test", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    words = line.split()
    bluePrints.append(BluePrint(words[6], words[12], words[18], words[21], words[27], words[30]))

# scenarios = {}
# path = Path(bluePrints[0])
# path.collect()
# path.collect()
# print(path.canProduce())
# path.produce(1)
# path.collect()
# path.collect()
# print(path.canProduce())
# path.produce(1)
# path.collect()
# path.collect()
# print(path.canProduce())
# path.produce(1)
# path.collect()
# path.collect()
# path.collect()
# path.collect()
# print(path.canProduce())
# print(path.robots)
# print(len([robot for robot in path.robots if robot != 0]))
# print(path.resources)
# path.produce(2)
# path.collect()
# print(path.canProduce())
# print(path.robots)
# print(len([robot for robot in path.robots if robot != 0]))
# print(path.resources)

totalScore = 0
for i, bluePrint in enumerate(bluePrints):
    paths = [Path(bluePrint)]
    skipped = [0,0,0]
    maxScore = 0
    pathsCompleted = 0
    scenarios = {}
    ot = time.time()
    while len(paths) > 0:
        path = paths.pop()
        options = path.canProduce()
        if len(options) < len([robot for robot in path.robots if robot != 0]):
            nothingPath = copy.deepcopy(path)
            nothingPath.collect()
            paths.append(nothingPath)
        else:
            skipped[1] += 1
        if 3 in options: options = [3]
        for robotToProduce in options:
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
            # if pathsCompleted % 100_000 == 0:
            #     print(pathsCompleted)
            #     print(skipped)
            #     print(maxScore)
            #     print(maxRobots)
            #     print(maxResources)
            #     print(maxProduced)
            #     print(path.produced)
            #     print(len(paths))
            #     print(len(scenarios))
            #     et = time.time()
            #     print(et-ot)
            #     ot = et
            paths.remove(path)
    totalScore += maxScore * (i + 1)
    print(i + 1, maxScore, totalScore)
    print(skipped)
    et = time.time()
    print(et-ot)
    ot = et

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
#2, 2, 2, 2, 52, 76, 118, 118, 118, 148, 148, 148