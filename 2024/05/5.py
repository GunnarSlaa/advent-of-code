def check_update(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                return False
    return True


def order_update(update, rules):
    for _ in range(len(update)):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                ind0 = update.index(rule[0])
                ind1 = update.index(rule[1])
                if ind1 < ind0:
                    update[ind0], update[ind1] = update[ind1], update[ind0]
    return update


with open("input", "r") as file:
    parts = file.read().strip().split("\n\n")

rules = parts[0].split("\n")
rules = [[int (_) for _ in rule.split("|")] for rule in rules]
updates = parts[1].split("\n")
updates = [[int (_) for _ in update.split(",")] for update in updates]

resulta = 0
resultb = 0

for update in updates:
    if check_update(update, rules):
        resulta += update[int((len(update) -1) / 2)]
    else:
        update = order_update(update, rules)
        resultb += update[int((len(update) -1) / 2)]

print(resulta)
print(resultb)