import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total1 = 0
total2 = 0

bag_dict ={}
for line in lines:
    bag_name = line.split(" bags ")[0]
    contains = line.split(" contain ")[1].split(", ")
    if contains[0] == "no other bags.":
        contains = []
    contains = [(c.split()[1] + " " + c.split()[2], c.split()[0]) for c in contains]
    bag_dict[bag_name] = contains

print(bag_dict)
valid = set()
prev_len = -1
while len(valid) != prev_len:
    prev_len = len(valid)
    for bag in bag_dict:
        if any(contains == "shiny gold" for contains, num in bag_dict[bag]):
            valid.add(bag)
        if any(contains in valid for contains, num in bag_dict[bag]):
            valid.add(bag)

def num_in_bag(bag):
    cnt = 1
    for contains, num in bag_dict[bag]:
        cnt += int(num) * num_in_bag(contains)
    return cnt

print(len(valid))
print(num_in_bag("shiny gold") - 1)
