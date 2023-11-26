import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
for line in lines:
    low = line.split("-")[0]
    high = line.split("-")[1].split(" ")[0]
    letter = line.split(" ")[1].split(":")[0]
    password = line.split(" ")[2]
    if (password[int(low) - 1] == letter) ^ (password[int(high) - 1] == letter):
        total += 1

print(total)