file = open("Input_1.txt", "r")
amount = 0
topthree = [0, 0, 0]
for line in file:
    if line in ['\n', '\r\n']:
        topthree.append(amount)
        topthree.sort()
        topthree = topthree[1:4]
        amount = 0
    else:
        amount += int(line)
print(topthree)
print(sum(topthree))
