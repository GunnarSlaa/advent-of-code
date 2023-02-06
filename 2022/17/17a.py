import copy
import time

def canMove(block, dir):
    # print(block)
    # print(dir)
    if dir == "<":
        for part in block:
            if part[0] == 0: return False
            if [part[0] - 1, part[1]] in grid: return False
        return True
    if dir == ">":
        for part in block:
            if part[0] == 6: return False
            if [part[0] + 1, part[1]] in grid: return False
        return True
    if dir == "d":
        for part in block:
            if part[1] == 0: return False
            if [part[0], part[1] - 1] in grid: return False
        return True

def Move(block, dir):
    #print("MOVE")
    if dir == "<":
        for part in block:
            part[0] -= 1
    if dir == ">":
        for part in block:
            part[0] += 1
    if dir == "d":
        for part in block:
            part[1] -= 1

def cleanGrid():
    global grid
    for y in reversed(range(height)):
        if all([[x, y] in grid for x in range(7)]):
            print(y)
            print("cleanGrid")
            #print("LEN_BEFORE: " + str(len(grid)))
            grid = [p for p in grid if p[1] >= y]
            #grid = [[p[0], p[1]-y] for p in grid if p[1] > y]
            return
            #print("LEN_AFTER: " + str(len(grid)))



st = time.time()

with open("input", "r") as f:
    jet = f.read().split("\n")[0]

shapes = ["####", ".#.-###-.#.", "..#-..#-###", "#-#-#-#", "##-##"]
shapeCoords = []
for shape in shapes:
    y = 3 + shape.count("-")
    x = 2
    shapeList = []
    for char in shape:
        if char == "#":
            shapeList.append([x, y])
            x += 1
        elif char == ".": x += 1
        elif char == "-":
            x = 2
            y -= 1
    shapeCoords.append(shapeList)

grid = []

jetIndex = 0
height = 0
prevHeight = 0
heightIncreases = []
for n in range(2022):
    if n % 500 == 0:
        print(n)
        cleanGrid()
    block = shapeCoords[n % 5]
    block = [[p[0], p[1] + height] for p in block]
    stopped = False
    while not stopped:
        if canMove(block, jet[jetIndex]): Move(block, jet[jetIndex])
        if canMove(block, "d"):
            Move(block, "d")
        else:
            stopped = True
            grid += block
        jetIndex += 1
        if jetIndex == len(jet):
            jetIndex = 0
    height = max([p[1] for p in grid]) + 1
print(height)
print(grid)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')