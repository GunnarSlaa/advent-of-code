import time

with open("input", "r") as f:
    lines = f.read().split("\n")

def canMove(pos, direction, empties):
    if direction == 0:
        if empties[0] and empties[1] and empties[2]:
            return (pos[0], pos[1] - 1)
        else:
            return None
    if direction == 1:
        if empties[2] and empties[3] and empties[4]:
            return (pos[0] + 1, pos[1])
        else:
            return None
    if direction == 2:
        if empties[4] and empties[5] and empties[6]:
            return (pos[0], pos[1] + 1)
        else:
            return None
    if direction == 3:
        if empties[6] and empties[7] and empties[0]:
            return (pos[0] - 1, pos[1])
        else:
            return None

def emptyPosAround(pos):
    positions = [(pos[0] - 1, pos[1] - 1),
                 (pos[0]    , pos[1] - 1),
                 (pos[0] + 1, pos[1] - 1),
                 (pos[0] + 1, pos[1]),
                 (pos[0] + 1, pos[1] + 1),
                 (pos[0]    , pos[1] + 1),
                 (pos[0] - 1, pos[1] + 1),
                 (pos[0] - 1, pos[1])]
    return [pos not in elves for pos in positions]

st = time.time()

elves = []

for y, row in enumerate(lines):
    for x, col in enumerate(row):
        if col == "#": elves.append((x, y))

moveList = [0,2,3,1]
moveDict = {"some": "thing"}
counter = 0
while len(moveDict.keys()) > 0:
    counter += 1
    moveDict = {}
    blocked = []
    for elf in elves:
        move = None
        empties = emptyPosAround(elf)
        if not all(empties):
            for dir in moveList:
                move = canMove(elf, dir, empties)
                if move: break
        if move:
            if move in moveDict.values():
                if move not in blocked:
                    blocked.append(move)
            else:
                moveDict[elf] = move
    moveDict = {key: val for key, val in moveDict.items() if val not in blocked}
    for elf, move in moveDict.items():
        elves.remove(elf)
        elves.append(move)
    moveList = moveList[1:] + [moveList[0]]
    if counter % 10 == 0:
        print(counter)
        print(len(moveDict.keys()), "/", len(elves))
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')


# print(elves)
# max0 = min(tup[1] for tup in elves)
# max1 = max(tup[0] for tup in elves)
# max2 = max(tup[1] for tup in elves)
# max3 = min(tup[0] for tup in elves)
# for col in range(max0, max2 + 1):
#     rowPrint = ""
#     for row in range(max3, max1 + 1):
#         if (row, col) in elves:
#             rowPrint += "#"
#         else:
#             rowPrint += "."
#     print(rowPrint)
print(counter)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')