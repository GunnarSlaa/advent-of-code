file = open("Input_5_clean.txt", "r")
Stacks = [
    "HBVWNMLP",
    "MQH",
    "NDBGFQML",
    "ZTFQMWG",
    "MTHP",
    "CBMJDHGT",
    "MNBFVR",
    "PLHMRGS",
    "PDBCN"
]
for line in file:
    amount = int(line.split()[1])
    stackFrom = int(line.split()[3]) - 1
    stackTo = int(line.split()[5]) - 1
    Stacks[stackTo] += Stacks[stackFrom][len(Stacks[stackFrom]) - amount:len(Stacks[stackFrom])]
    Stacks[stackFrom] = Stacks[stackFrom][0:len(Stacks[stackFrom]) - amount]
    print(Stacks)
