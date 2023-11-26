import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

numbers = [int(c) for c in lines]
numbers.append(0)
numbers.sort()
ones = 0
threes = 1
arrangements = [0] * len(numbers)
arrangements[0] = 1
for i in range(len(numbers) - 1):
    if numbers[i+1] - numbers[i] == 1:
        ones += 1
    elif numbers[i+1] - numbers[i] == 3:
        threes += 1
    for j in range(1, 4):
        if i + j > len(numbers) - 1: continue
        if numbers[i + j] <= numbers[i] + 3:
            arrangements[i + j] += arrangements[i]

print(ones * threes)
print(arrangements[-1])