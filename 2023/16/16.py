from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

g = grid_from_lines(lines)


def run_beam(beam):
    visited = set()
    beams = set()
    beams.add(beam)
    while beams:
        new_beams = set()
        for beam in beams:
            visited.add(beam)
            next_field = get_neighbour_dir(g, beam[0], beam[1], beam[2])
            if not next_field:
                continue
            elif g[next_field[0]][next_field[1]] == "-":
                if beam[2] == 1 or beam[2] == 3:
                    new_beams.add((next_field[0], next_field[1], beam[2]))
                else:
                    new_beams.add((next_field[0], next_field[1], 1))
                    new_beams.add((next_field[0], next_field[1], 3))
            elif g[next_field[0]][next_field[1]] == "|":
                if beam[2] == 0 or beam[2] == 2:
                    new_beams.add((next_field[0], next_field[1], beam[2]))
                else:
                    new_beams.add((next_field[0], next_field[1], 0))
                    new_beams.add((next_field[0], next_field[1], 2))
            elif g[next_field[0]][next_field[1]] == "/":
                if beam[2] == 0:
                    new_beams.add((next_field[0], next_field[1], 1))
                elif beam[2] == 1:
                    new_beams.add((next_field[0], next_field[1], 0))
                elif beam[2] == 2:
                    new_beams.add((next_field[0], next_field[1], 3))
                elif beam[2] == 3:
                    new_beams.add((next_field[0], next_field[1], 2))
            elif g[next_field[0]][next_field[1]] == "\\":
                if beam[2] == 0:
                    new_beams.add((next_field[0], next_field[1], 3))
                elif beam[2] == 1:
                    new_beams.add((next_field[0], next_field[1], 2))
                elif beam[2] == 2:
                    new_beams.add((next_field[0], next_field[1], 1))
                elif beam[2] == 3:
                    new_beams.add((next_field[0], next_field[1], 0))
            elif g[next_field[0]][next_field[1]] == ".":
                new_beams.add((next_field[0], next_field[1], beam[2]))
        beams = new_beams - visited
    energized = set([(c[0], c[1]) for c in visited])
    return len(energized)


print(run_beam((0, -1, 1)) - 1)

answer = 0
for row in range(len(g)):
    answer = max(answer, run_beam((row, 0, 1)))
    answer = max(answer, run_beam((row, len(g[0]) - 1, 3)))
for col in range(len(g[0])):
    answer = max(answer, run_beam((0, col, 2)))
    answer = max(answer, run_beam((len(g) - 1, col, 0)))

print(answer)

