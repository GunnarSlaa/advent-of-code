with open("input_test", "r") as file:
    blocks = file.read().strip().split("\n\n")

workflows = {}
for workflow in blocks[0].split("\n"):
    workflows[workflow.split("{")[0]] = workflow.split("{")[1].split("}")[0]

parts = []
for part in blocks[1].split("\n"):
    p = {}
    for rule in part[1:-1].split(","):
        p[rule[0]] = int(rule[2:])
    parts.append(p)


def test_part(part, wf):
    for rule in workflows[wf].split(","):
        if rule == "A":
            return True
        elif rule == "R":
            return False
        elif ":" not in rule:
            return test_part(part, rule)
        else:
            if "<" in rule:
                if part[rule.split("<")[0]] < int(rule.split("<")[1].split(":")[0]):
                    if rule.split(":")[1] == "A":
                        return True
                    elif rule.split(":")[1] == "R":
                        return False
                    else:
                        return test_part(part, rule.split(":")[1])
            elif ">" in rule:
                if part[rule.split(">")[0]] > int(rule.split(">")[1].split(":")[0]):
                    if rule.split(":")[1] == "A":
                        return True
                    elif rule.split(":")[1] == "R":
                        return False
                    else:
                        return test_part(part, rule.split(":")[1])


total = 0
for part in parts:
    if test_part(part, "in"):
        total += sum(part.values())
print(total)
