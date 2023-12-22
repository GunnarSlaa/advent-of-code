with open("input", "r") as file:
    lines = file.read().strip().split("\n")

blocks = []
for line in lines:
    a = [int(c) for c in line.split("~")[0].split(",")]
    b = [int(c) for c in line.split("~")[1].split(",")]
    block = [tuple(a), tuple(b)]
    if a == b:
        block = [tuple(a)]
    elif a[0] != b[0]:
        start = min(a[0], b[0])
        end = max(a[0], b[0])
        block.extend([(i, a[1], a[2]) for i in range(start + 1, end)])
    elif a[1] != b[1]:
        start = min(a[1], b[1])
        end = max(a[1], b[1])
        block.extend([(a[0], i, a[2]) for i in range(start + 1, end)])
    elif a[2] != b[2]:
        start = min(a[2], b[2])
        end = max(a[2], b[2])
        block.extend([(a[0], a[1], i) for i in range(start + 1, end)])
    blocks.append(block)

landed_cubes = {}
block_positions = {}
blocks.sort(key=lambda t: min(t[0][2], t[-1][2]))
for i, block in enumerate(blocks):
    while min(block[0][2], block[-1][2]) > 1:
        if any([(cube[0], cube[1], cube[2] - 1) in landed_cubes.keys() for cube in block]):
            break
        block = [(cube[0], cube[1], cube[2] - 1) for cube in block]
    for cube in block:
        landed_cubes[cube] = i
    block_positions[i] = block

supports = [set() for _ in range(len(block_positions))]
supported_by = [set() for _ in range(len(block_positions))]
for i, block in block_positions.items():
    for cube in block:
        if (cube[0], cube[1], cube[2] + 1) in landed_cubes and landed_cubes[(cube[0], cube[1], cube[2] + 1)] != i:
            supports[i].add(landed_cubes[(cube[0], cube[1], cube[2] + 1)])
            supported_by[landed_cubes[(cube[0], cube[1], cube[2] + 1)]].add(i)

answer1 = 0
answer2 = 0
for remove in range(len(supports)):
    found = set()
    frontier = set()
    frontier.add(remove)
    while frontier:
        found.update(frontier)
        new_frontier = set()
        for f in frontier:
            for s in supports[f]:
                if all([c in found for c in supported_by[s]]):
                    new_frontier.add(s)
        frontier = new_frontier
    if len(found) == 1:
        answer1 += 1
    answer2 += len(found) - 1

print(answer1)
print(answer2)
