with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

seeds = [int(c) for c in lines[0].split(": ")[1].split()]
maps = []
for line in lines[1:]:
    m = []
    for l in line.split("\n")[1:]:
        m.append([int(c) for c in l.split()])
    maps.append(m)


def map_to(source, map):
    for r in map:
        if r[1] <= source <= r[1] + r[2] - 1:
            return r[0] + (source - r[1])
    return source
        

locations = []
for map in maps:
    seeds = [map_to(seed, map) for seed in seeds]

print(min(seeds))
