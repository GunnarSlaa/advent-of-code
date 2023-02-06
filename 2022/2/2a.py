scoreDict = {}
moveScoreDict = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

for opponent_move in ['A', 'B', 'C']:
    for my_move in ['X', 'Y', 'Z']:
        score = moveScoreDict[my_move]
        move_diff = (ord(my_move) - ord(opponent_move)) % 3
        if move_diff == 0:
            score += 6
        elif move_diff == 1:
            score += 0
        elif move_diff == 2:
            score += 3
        scoreDict[opponent_move + ' ' + my_move] = score

file = open("Input2.txt", "r")
totalScore = 0
for line in file:
    totalScore += scoreDict[line.strip()]
print(totalScore)

