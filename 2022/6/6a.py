file = open("Input6.txt", "r")
for line in file:
    for i in range(len(line) - 14):
        if len("".join(set(line[i:i+14]))) == 14:
            print(i + 14)
            break
