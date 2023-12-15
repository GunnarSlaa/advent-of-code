with open("input", "r") as file:
    parts = file.read().strip().split(",")

boxes = [{} for _ in range(256)]
for part in parts:
    box = 0
    label = part.split("-")[0].split("=")[0]
    for c in list(label):
        box += ord(c)
        box *= 17
        box %= 256
    if "-" in part:
        if label in boxes[box].keys():
            boxes[box].pop(label)
    elif "=" in part:
        focal = int(part.split("=")[1])
        boxes[box][label] = focal

answer = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box.values()):
        answer += (i + 1) * (j + 1) * lens

print(answer)
