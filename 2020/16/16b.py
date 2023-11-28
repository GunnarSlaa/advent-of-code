import numpy as np

with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

rules = [line.split(": ")[1].split()[0] for line in lines[0].split("\n")]
rules.extend([line.split()[-1] for line in lines[0].split("\n")])
rules = [rule.split("-") for rule in rules]
rules = [[int(part) for part in rule] for rule in rules]

my_ticket = [int(field) for field in lines[1].split("\n")[1].split(",")]

other_tickets = lines[2].split("\n")[1:]
other_tickets = [ticket.split(",") for ticket in other_tickets]
other_tickets = [[int(field) for field in ticket] for ticket in other_tickets]


def check_field(field, check_rules):
    return any([rule[0] <= field <= rule[1] for rule in check_rules])


valid_tickets = [ticket for ticket in other_tickets if all([check_field(field, rules) for field in ticket])]
valid_tickets.append(my_ticket)
num_rules = int(len(rules)/2)
rulesets = [[rules[i], rules[i + num_rules]] for i in range(num_rules)]


poss_list = []
for ruleset in rulesets:
    possibilities = list(range(len(my_ticket)))
    for ticket in valid_tickets:
        possibilities = [poss for poss in possibilities if check_field(ticket[poss], ruleset)]
    poss_list.append(possibilities)
done_list = []
while len(done_list) < num_rules:
    for poss in poss_list:
        if len(poss) == 1 and poss[0] not in done_list:
            for poss2 in poss_list:
                if len(poss2) > 1:
                    poss2.remove(poss[0])
            done_list.append(poss[0])
dep_fields = [my_ticket[c[0]] for c in poss_list[:6]]
# Number too big for np.prod
print(dep_fields[0] * dep_fields[1] * dep_fields[2] * dep_fields[3] * dep_fields[4] * dep_fields[5])
