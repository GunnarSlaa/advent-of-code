tailPos = [0,0]
headPos = [0,0]
tailSet = {"0,0"}


def moveTail():
    #No move
    if abs(headPos[0] - tailPos[0]) <= 1 and abs(headPos[1] - tailPos[1]) <= 1: return
    #Diagonal move
    if headPos[0] >= tailPos[0] + 1 and headPos[1] >= tailPos[1] + 1:
        tailPos[0] += 1
        tailPos[1] += 1
    elif headPos[0] >= tailPos[0] + 1 and headPos[1] <= tailPos[1] - 1:
        tailPos[0] += 1
        tailPos[1] -= 1
    elif headPos[0] <= tailPos[0] - 1 and headPos[1] >= tailPos[1] + 1:
        tailPos[0] -= 1
        tailPos[1] += 1
    elif headPos[0] <= tailPos[0] - 1 and headPos[1] <= tailPos[1] - 1:
        tailPos[0] -= 1
        tailPos[1] -= 1
    #Straight move:
    elif headPos[0] >= tailPos[0] + 2: tailPos[0] += 1
    elif headPos[0] <= tailPos[0] - 2: tailPos[0] -= 1
    elif headPos[1] >= tailPos[1] + 2: tailPos[1] += 1
    elif headPos[1] <= tailPos[1] - 2: tailPos[1] -= 1
    tailSet.add(str(tailPos[0]) + "," + str(tailPos[1]))


def moveHead(direction):
    if direction == "U": headPos[1] += 1
    elif direction == "D": headPos[1] -= 1
    elif direction == "L": headPos[0] -= 1
    elif direction == "R": headPos[0] += 1


def move(direction, times):
    for i in range(int(times)):
        moveHead(direction)
        moveTail()
        print(tailPos, headPos)


with open("Input9.txt", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    move(line.split(" ")[0], line.split(" ")[1])

print(tailSet)
print(len(tailSet))