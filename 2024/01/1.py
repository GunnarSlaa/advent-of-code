with open("input", "r") as file:
    lines = file.read().strip().split("\n")

list1 = []
list2 = []
for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()
result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

print(result)