scoreDict = {}
moveScoreDict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
resultDict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
opponentMoveList = ['A', 'B', 'C']
moveList = ['X', 'Y', 'Z']

for opponentMove in opponentMoveList:
    for requiredResult in ['X', 'Y', 'Z']:
        opponentMoveIndex = opponentMoveList.index(opponentMove)
        move = ""
        if requiredResult == 'X':
            moveIndex = (opponentMoveIndex + 2) % 3
            move = moveList[moveIndex]
        elif requiredResult == 'Y':
            move = moveList[opponentMoveIndex]
        elif requiredResult == 'Z':
            moveIndex = (opponentMoveIndex + 1) % 3
            move = moveList[moveIndex]
        score = moveScoreDict[move] + resultDict[requiredResult]
        scoreDict[opponentMove + ' ' + requiredResult] = score
print(scoreDict)
file = open("Input2.txt", "r")
totalScore = 0
for line in file:
    totalScore += scoreDict[line.strip()]
print(totalScore)

