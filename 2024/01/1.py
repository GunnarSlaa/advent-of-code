with open("input", "r") as file:
    lines = file.read().strip().split("\n")

list1 = sorted([int(line.split()[0]) for line in lines])
list2 = sorted([int(line.split()[1]) for line in lines])

result = sum([abs(list1[i] - list2[i]) for i in range(len(list1))])

print(result)