with open("input", "r") as file:
    parts = file.read().strip().split(",")

answer = 0
for part in parts:
    current = 0
    for c in list(part):
        current += ord(c)
        current *= 17
        current %= 256
    answer += current

print(answer)
