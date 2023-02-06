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


def moveIntoDir(dir, currentPath):
    return currentPath + "/" + dir


def moveDirUp(currentPath):
    path = currentPath.rsplit("/", 1)[0]
    if path == "": path = "/"
    return path


def readDir(currentPath, i):
    name = currentPath
    directSize = 0
    subDirs = []
    for j in range(1, 1000):
        if len(lines) == i + j or lines[i + j].startswith("$"):
            break
        elif lines[i + j].startswith("dir"):
            subDirName = lines[i + j].split(" ")[1]
            subDirs.append(moveIntoDir(subDirName, currentPath))
        else:
            directSize += int(lines[i + j].split(" ")[0])
    dirDict[name] = Directory(name, directSize, subDirs)


dirDict = {}
totalSizeDict = {}

with open("Input7.txt", "r") as f:
    lines = f.read().split("\n")

pwd = "/"
for i in range(len(lines)):
    if lines[i] == "$ cd ..": pwd = moveDirUp(pwd)
    elif lines[i].startswith("$ cd"): pwd = moveIntoDir(lines[i].split(" ")[2], pwd)
    elif lines[i] == ("$ ls"): readDir(pwd, i)

for dir in dirDict.values():
    dir.calculateSize()

totalUnder10000 = 0
for dirTotalSize in totalSizeDict.values():
    if dirTotalSize <= 100000:
        totalUnder10000 += dirTotalSize

minDeleted = 1000000000
for dirTotalSize in totalSizeDict.values():
    if dirTotalSize >= 8748071 and dirTotalSize < minDeleted:
        minDeleted = dirTotalSize
print(totalUnder10000)
print(totalSizeDict["/"])
print(minDeleted)
