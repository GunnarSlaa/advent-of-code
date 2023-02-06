with open("input_test", "r") as f:
    lines = f.read().split("\n")

monkeyDict = {}
calcList = []

for line in lines:
    words = line.split()
    name = words[0].split(":")[0]
    if len(words) == 2:
        monkeyDict[name] = int(words[1])
    else:
        calc = [name, words[1], words[2], words[3]]
        calcList.append(calc)

print(monkeyDict)
print(calcList)

while len(calcList) > 0:
    toRemove = []
    for calc in calcList:
        if calc[1] in monkeyDict.keys() and calc[3] in monkeyDict.keys():
            toRemove.append(calc)
            result = eval(str(monkeyDict[calc[1]]) + calc[2] + str(monkeyDict[calc[3]]))
            monkeyDict[calc[0]] = result
    for calc in toRemove:
        calcList.remove(calc)

print(monkeyDict['root'])


