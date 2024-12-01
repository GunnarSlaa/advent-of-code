with open("input", "r") as file:
    lines = file.read().strip().split("\n")

list1 = sorted([int(line.split()[0]) for line in lines])
list2 = sorted([int(line.split()[1]) for line in lines])

result = sum([i * list2.count(i) for i in list1])

print(result)