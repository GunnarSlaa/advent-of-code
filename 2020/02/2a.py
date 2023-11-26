import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
for line in lines:
    min = line.split("-")[0]
    max = line.split("-")[1].split(" ")[0]
    letter = line.split(" ")[1].split(":")[0]
    password = line.split(" ")[2]
    if int(min) <= password.count(letter) <= int(max):
        total += 1

print(total)
