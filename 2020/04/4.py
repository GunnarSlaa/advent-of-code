import itertools

with open("input", "r") as file:
    lines = file.read().strip().split("\n\n")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def check1(dict_fields):
    for field in fields:
        if field not in dict_fields.keys():
            return False
    return True


def check_number(number, length, mini, maxi):
    if len(number) != length:
        return False
    if any(not c.isdigit() for c in number):
        return False
    return mini <= int(number) <= maxi


def check2(dict_fields):
    if not check1(dict_fields):
        return False
    if not check_number(dict_fields["byr"], 4, 1920, 2002):
        return False
    if not check_number(dict_fields["iyr"], 4, 2010, 2020):
        return False
    if not check_number(dict_fields["eyr"], 4, 2020, 2030):
        return False
    if dict_fields["hgt"][-2:] == "cm":
        if not check_number(dict_fields["hgt"][:-2], 3, 150, 193):
            return False
    elif dict_fields["hgt"][-2:] == "in":
        if not check_number(dict_fields["hgt"][:-2], 2, 59, 76):
            return False
    else:
        return False
    if dict_fields["hcl"][0] != "#":
        return False
    if len(dict_fields["hcl"]) != 7:
        return False
    if any(c not in "01234567890abcdef" for c in dict_fields["hcl"][1:]):
        return False
    if dict_fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not check_number(dict_fields["pid"], 9, 0, 999999999):
        return False
    return True


count1 = 0
count2 = 0
for line in lines:
    dict_fields = {}
    for part in line.split():
        dict_fields[part.split(":")[0]] = part.split(":")[1]
    count1 += check1(dict_fields)
    count2 += check2(dict_fields)

print(count1)
print(count2)
