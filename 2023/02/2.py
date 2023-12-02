import re

with open("2023/02/input", "r") as file:
    lines = file.read().strip().split("\n")

games = []
for line in lines:
    game = line.split(": ")[1].split("; ")
    game = [turn.split(", ") for turn in game]
    games.append(game)


def checkgame(game):
    for turn in game:
        for move in turn:
            if move.split()[1] == "red" and int(move.split()[0]) > 12:
                return False
            elif move.split()[1] == "green" and int(move.split()[0]) > 13:
                return False
            elif move.split()[1] == "blue" and int(move.split()[0]) > 14:
                return False
    return True


def power(game):
    rgb = [0,0,0]
    for turn in game:
        for move in turn:
            if move.split()[1] == "red" and int(move.split()[0]) > rgb[0]:
                rgb[0] = int(move.split()[0])
            elif move.split()[1] == "green" and int(move.split()[0]) > rgb[1]:
                rgb[1] = int(move.split()[0])
            elif move.split()[1] == "blue" and int(move.split()[0]) > rgb[2]:
                rgb[2] = int(move.split()[0])
    return rgb[0] * rgb[1] * rgb[2]


print(sum([i + 1 for i, game in enumerate(games) if checkgame(game)]))
print(sum([power(game) for game in games]))