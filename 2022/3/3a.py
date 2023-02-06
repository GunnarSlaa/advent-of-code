file = open("input3.txt", "r")
total = 0
def value(char):
    charValue = ord(char) - 96
    if charValue < 0: charValue += 58
    return charValue

for line in file:
    cutOff = int(len(line)/2)
    firstPart = line[0:cutOff]
    secondPart = line[cutOff:]
    for char in firstPart:
        if char in secondPart:
            total += value(char)
            print(char, value(char))
            break
print(total)