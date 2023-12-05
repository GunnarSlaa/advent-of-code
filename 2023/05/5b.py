with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

seeds = [int(c) for c in lines[0].split(": ")[1].split()]
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append([seeds[i], seeds[i] + seeds[i+1] - 1])

maps = []
for line in lines[1:]:
    m = []
    for l in line.split("\n")[1:]:
        m.append([int(c) for c in l.split()])
    maps.append(m)


def map_range(range, map):
    ranges = [range]
    new_ranges = []
    for r in map:
        next_ranges = []
        for range in ranges:
            if range[0] < r[1] < range[1] <= r[1] + r[2] - 1:
                next_ranges.append([range[0], r[1] - 1])
                new_ranges.append([r[0], r[0] + range[1] - r[1]])
            elif r[1] <= range[0] < r[1] + r[2] - 1 < range[1]:
                next_ranges.append([r[1] + r[2], range[1]])
                new_ranges.append([r[0] + range[0] - r[1], r[0] + r[2] - 1])
            elif range[0] >= r[1] and range[1] <= r[1] + r[2] - 1: 
                new_ranges.append([range[0] + r[0] - r[1], range[1] + r[0] - r[1]])
            elif range[0] < r[1] and range[1] > r[1] + r[2] - 1:
                next_ranges.append([range[0], r[1] - 1])
                new_ranges.append([r[0], r[0] + r[2] - 1])
                next_ranges.append([r[1] + r[2], range[1]])
            else:
                next_ranges.append(range)
        ranges = next_ranges
    new_ranges.extend(ranges)
    return new_ranges

        
for map in maps:
    new_seed_ranges = []
    for range in seed_ranges:
        new_seed_ranges.extend(map_range(range, map))
    seed_ranges = new_seed_ranges

print(min([c[0] for c in seed_ranges]))
        