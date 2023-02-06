ropePos = [[0,0] for i in range(10)]
tailSet = {"0,0"}


def moveTail(tailNum):
    print(tailNum)
    #No move
    if abs(ropePos[tailNum-1][0] - ropePos[tailNum][0]) <= 1 and abs(ropePos[tailNum-1][1] - ropePos[tailNum][1]) <= 1: return
    #Diagonal move
    if ropePos[tailNum-1][0] >= ropePos[tailNum][0] + 1 and ropePos[tailNum-1][1] >= ropePos[tailNum][1] + 1:
        ropePos[tailNum][0] += 1
        ropePos[tailNum][1] += 1
    elif ropePos[tailNum-1][0] >= ropePos[tailNum][0] + 1 and ropePos[tailNum-1][1] <= ropePos[tailNum][1] - 1:
        ropePos[tailNum][0] += 1
        ropePos[tailNum][1] -= 1
    elif ropePos[tailNum-1][0] <= ropePos[tailNum][0] - 1 and ropePos[tailNum-1][1] >= ropePos[tailNum][1] + 1:
        ropePos[tailNum][0] -= 1
        ropePos[tailNum][1] += 1
    elif ropePos[tailNum-1][0] <= ropePos[tailNum][0] - 1 and ropePos[tailNum-1][1] <= ropePos[tailNum][1] - 1:
        ropePos[tailNum][0] -= 1
        ropePos[tailNum][1] -= 1
    #Straight move:
    elif ropePos[tailNum-1][0] >= ropePos[tailNum][0] + 2: ropePos[tailNum][0] += 1
    elif ropePos[tailNum-1][0] <= ropePos[tailNum][0] - 2: ropePos[tailNum][0] -= 1
    elif ropePos[tailNum-1][1] >= ropePos[tailNum][1] + 2: ropePos[tailNum][1] += 1
    elif ropePos[tailNum-1][1] <= ropePos[tailNum][1] - 2: ropePos[tailNum][1] -= 1
    if tailNum == 9: tailSet.add(str(ropePos[tailNum][0]) + "," + str(ropePos[tailNum][1]))


def moveHead(direction):
    if direction == "U": ropePos[0][1] += 1
    elif direction == "D": ropePos[0][1] -= 1
    elif direction == "L": ropePos[0][0] -= 1
    elif direction == "R": ropePos[0][0] += 1


def move(direction, times):
    for i in range(int(times)):
        moveHead(direction)
        for j in range(1,10):
            moveTail(j)


with open("Input9.txt", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    move(line.split(" ")[0], line.split(" ")[1])

print(tailSet)
print(len(tailSet))