with open("input", "r") as file:
    lines = file.read().strip().split("\n")

list1 = []
list2 = []
for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

result = 0
for i in list1:
    result += i * list2.count(i)

print(result)