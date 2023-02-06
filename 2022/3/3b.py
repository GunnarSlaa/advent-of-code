file = open("input3.txt", "r")
total = 0
numberInGroup = 0
group = [""] * 3


def value(character):
    charValue = ord(character) - 96
    if charValue < 0: charValue += 58
    return charValue


for line in file:
    group[numberInGroup] = line
    if numberInGroup != 2:
        numberInGroup += 1
        continue
    numberInGroup = 0
    for char in group[0]:
        if char in group[1] and char in group[2]:
            total += value(char)
            break
print(total)
