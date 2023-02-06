import copy, re
with open("input", "r") as f:
    lines = f.read().split("\n")

monkeyDict = {}
calcList = []

for line in lines:
    words = line.split()
    name = words[0].split(":")[0]
    if len(words) == 2:
        monkeyDict[name] = int(words[1])
    else:
        calc = [name, words[1], words[3], words[1] + words[2] + words[3]]
        calcList.append(calc)

monkeyDictOrig = copy.deepcopy(monkeyDict)
print(monkeyDict)
print(calcList)

monkeyDict['humn'] = 'x'
while len(calcList) > 0:
    toRemove = []
    for calc in calcList:
        if calc[1] in monkeyDict.keys() and calc[2] in monkeyDict.keys():
            toRemove.append(calc)
            part1 = str(monkeyDict[calc[1]])
            part2 = str(monkeyDict[calc[2]])
            if calc[0] == 'root':
                root1 = part1
                root2 = part2
                break
            if calc[1] not in monkeyDictOrig.keys():
                part1 = "(" + part1 + ")"
            if calc[2] not in monkeyDictOrig.keys():
                part2 = "(" + part2 + ")"
            result = calc[3].replace(calc[1], part1).replace(calc[2], part2)
            if 'x' not in result:
                result = eval(result)
                monkeyDictOrig[calc[0]] = result
            monkeyDict[calc[0]] = result
    for calc in toRemove:
        calcList.remove(calc)

print(root1)
root1Keep = copy.deepcopy(root1)
root2Keep = copy.deepcopy(root2)
print(root2)
root3 = float(root2)
root2 = float(root2)
while "(" in root1:
    calc = [_ for _ in re.split("\(.*\)", root1) if _ != ''][0]
    root1 = re.search("\(.*\)", root1).group()[1:- 1]
    if "+" in calc:
        root3 -= float(calc.replace("+", ""))
        #print(calc, root2, root3)
        root2 = root3
    elif "-" in calc:
        if calc.endswith("-"):
            root3 = float(calc.replace("-", "")) - root3
        else:
            root3 += float(calc.replace("-", ""))
        #print(calc, root2, root3)
        root2 = root3
    elif "/" in calc:
        root3 *= float(calc.replace("/", ""))
        #print(calc, root2, root3)
        root2 = root3
    elif "*" in calc:
        root3 /= float(calc.replace("*", ""))
        #print(calc, root2, root3)
        root2 = root3
    #print(root1, calc)
print(root1, root2)
print(root2 + 568)
print(eval(root1Keep.replace('x', str(root2 + 568))))
print(root2Keep)


