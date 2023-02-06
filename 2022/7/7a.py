class Directory:
    name: str
    directSize: int
    subDirs: list

    def __init__(self, name, directSize, subDirs):
        self.name = name
        self.directSize = directSize
        self.subDirs = subDirs

    def calculateSize(self):
        if self.name in totalSizeDict: return totalSizeDict[self.name]
        size = self.directSize
        for subDir in self.subDirs:
            size += dirDict[subDir].calculateSize()
        totalSizeDict[self.name] = size
        return size


dirDict = {}
totalSizeDict = {}

with open("Input7.txt", "r") as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    if lines[i].endswith(" ls"):
        name = lines[i - 1].split(" ")[2]
        directSize = 0
        subDirs = []
        for j in range(1, 1000):
            if len(lines) == i + j or lines[i + j].startswith("$"):
                break
            elif lines[i + j].startswith("dir"):
                subDirs.append(lines[i + j].split(" ")[1])
            else:
                directSize += int(lines[i + j].split(" ")[0])
        if name in dirDict: print("WOOPS!", name)
        dirDict[name] = Directory(name, directSize, subDirs)

print(dirDict)

for dir in dirDict.values():
    dir.calculateSize()

print(totalSizeDict)

totalUnder10000 = 0
for totalSize in totalSizeDict.values():
    if totalSize <= 100000:
        totalUnder10000 += totalSize
print(totalUnder10000)