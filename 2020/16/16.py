from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

rules = [line.split(": ")[1].split()[0] for line in lines[0].split("\n")]
rules.extend([line.split()[-1] for line in lines[0].split("\n")])
rules = [rule.split("-") for rule in rules]
rules = [[int(part) for part in rule] for rule in rules]

other_tickets = lines[2].split("\n")[1:]
other_tickets = [ticket.split(",") for ticket in other_tickets]
other_tickets = [[int(field) for field in ticket] for ticket in other_tickets]


def check_field(field):
    return any([rule[0] <= field <= rule[1] for rule in rules])


total = 0
for ticket in other_tickets:
    total += sum([field for field in ticket if not check_field(field)])

print(total)
