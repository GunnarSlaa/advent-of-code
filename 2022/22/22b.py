import re

with open("input_test", "r") as f:
    lines = f.read().split("\n")
squareSize = 4
borders = {1: [[2, 0], [6, 1], [4, 0], [3, 0]],
           2: [[1, 0], [3, 3], [5, 2], [6, 2]],
           3: [[1, 3], [4, 3], [5, 3], [2, 1]],
           4: [[1, 2], [6, 0], [5, 0], [3, 1]],
           5: [[4, 2], [6, 3], [2, 2], [3, 2]],
           6: [[4, 1], [1, 1], [2, 3], [5, 1]]}

# borders = {1: [[6, 3], [2, 3], [3, 0], [4, 3]],
#            2: [[6, 2], [5, 1], [3, 1], [1, 1]],
#            3: [[1, 2], [2, 2], [5, 0], [4, 0]],
#            4: [[3, 3], [5, 3], [6, 0], [1, 3]],
#            5: [[3, 2], [2, 1], [6, 1], [4, 1]],
#            6: [[4, 2], [5, 2], [2, 0], [1, 0]]}

def neighbour(direction, cell):
    if direction == 0:
        direct = (cell[0], cell[1] - 1)
    elif direction == 1:
        direct = (cell[0] + 1, cell[1])
    elif direction == 2:
        direct = (cell[0], cell[1] + 1)
    elif direction == 3:
        direct = (cell[0] - 1, cell[1])
    if direct in grid:
        return direct
    else:
        print("Over de rand")

def move(direction, cell):
    nb = neighbour(direction, cell)
    if nb in grid:
        return grid[nb] == '.'
    else: print("PANIC!!")

def turn(direction, LR):
    if LR == "R": return (direction + 1) % 4
    else: return (direction + 3) % 4

length = max([len(line) for line in lines[:-2]])
rowSizes = []
colSizes = []
grid = {}
squares = {}
squareNum = 1
for row, line in enumerate(lines[:-2]):
    size = [len(re.split('#|\.', line)[0]), len(line) - 1]
    rowSizes.append(size)
    for i, col in enumerate(range(size[0], size[1] + 1)):
        grid[(col, row)] = line[col]
        squares[(col, row)] = i // squareSize + squareNum
    if (row + 1) % squareSize == 0:
        squareNum += int((size[1] + 1 - size[0]) / squareSize)
for col in range(length):
    start = min([tup[1] for tup in grid if tup[0] == col])
    end = max([tup[1] for tup in grid if tup[0] == col])
    colSizes.append([start, end])

print(squares)
squareBorders = []
for square in range(6):
    max0 = min(tup[1] for tup in squares.keys() if squares[tup] == square + 1)
    max1 = max(tup[0] for tup in squares.keys() if squares[tup] == square + 1)
    max2 = max(tup[1] for tup in squares.keys() if squares[tup] == square + 1)
    max3 = min(tup[0] for tup in squares.keys() if squares[tup] == square + 1)
    squareBorders.append([max0, max1, max2, max3])

print(squareBorders)

pos = (8,0)
face = 1

moves = re.split('R|L', lines[-1])
turns = [_ for _ in re.split('\d', lines[-1]) if _ != '']
print(len(moves), len(turns))
print(moves)
for nextMove in range(len(moves)):
    for _ in range(int(moves[nextMove])):
        if move(face, pos):
            pos = neighbour(face, pos)
        else:
            break
    if nextMove != len(moves) - 1: face = turn(face, turns[nextMove])
print((1000 * (pos[1] + 1)) + (4 * (pos[0] + 1)) + ((face + 3) % 4))