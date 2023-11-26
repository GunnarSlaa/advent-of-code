import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

numbers = [int(c) for c in lines]

for i in range(25, len(numbers)):
    preamble = [int(c) for c in numbers[i-25:i]]
    combinations = list(itertools.combinations(preamble, 2))
    valids = set([sum(c) for c in combinations])
    if numbers[i] not in valids:
        ans1 = numbers[i]
        print(ans1)
        break

for i in range(len(numbers)):
    j = 0
    rng = [numbers[i]]
    while sum(rng) < ans1:
        j += 1
        rng.append(numbers[i+j])
    if sum(rng) == ans1:
        print(max(rng) + min(rng))
        break


