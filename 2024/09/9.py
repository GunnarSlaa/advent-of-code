from grid_utils import *
import itertools
from copy import deepcopy

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

line = lines[0]
line = line + "0"

files = []
empty = []
position = 0

for i in range(int(len(line) / 2)):
    filesize = int(line[i * 2])
    files.append(list(range(position, position + filesize)))
    position += filesize
    emptyspace = int(line[i * 2 + 1])
    empty.extend(range(position, position + emptyspace))
    position += emptyspace

files_to_move = deepcopy(files)
files_to_move.reverse()

moved = 0
for space in empty:
    if files_to_move[0][0] < space:
        files[len(files_to_move) - 1] = files_to_move[0]
        break
    files_to_move[0][-1 - moved] = space
    moved += 1
    if moved == len(files_to_move[0]):
        moved = 0
        files[len(files_to_move) - 1] = files_to_move[0]
        del files_to_move[0]


result = 0
for i, x in enumerate(files):
    result += sum([i * f for f in x])

print(result)
