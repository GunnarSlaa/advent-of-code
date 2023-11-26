import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

instructions = [line.split() for line in lines]

def run(run_instructions):
    acc = 0
    current = 0
    ran = []
    while current not in ran and current < len(run_instructions):
        ran.append(current)
        if run_instructions[current][0] == "nop":
            current += 1
        elif run_instructions[current][0] == "acc":
            acc += int(run_instructions[current][1])
            current += 1
        elif run_instructions[current][0] == "jmp":
            current += int(run_instructions[current][1])
    return (current not in ran, acc)

print(run(instructions)[1])

for i in range(len(instructions)):
    if instructions[i][0] == "acc": continue
    if instructions[i][0] == "jmp":
        new_instructions = instructions[:i] + [["nop", instructions[i][1]]] + instructions[i+1:]
    elif instructions[i][0] == "nop":
        new_instructions = instructions[:i] + [["jmp", instructions[i][1]]] + instructions[i+1:]
    # print(new_instructions)
    if run(new_instructions)[0]:
        print(run(new_instructions)[1])