import functools

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

total = 0
total2 = 0

@functools.cache
def calc_line(str, lst):
    if len(lst) == 0:
        return "#" not in str
    if not "?" in str:
        return tuple([len(c) for c in str.split(".") if len(c) != 0]) == lst
    if len(str) < sum(lst) + len(lst) - 1:
        return 0
    answer = 0
    for i in range(len(str)):
        if len(str) - i < sum(lst) + len(lst) - 1:
            break
        if "#" in str[:i]:
            break    
        if "." in str[i:i + lst[0]]:
            continue
        if i + lst[0] < len(str) and str[i + lst[0]] == "#":
            continue
        answer += calc_line(str[i+lst[0]+1:], lst[1:])
    return answer


for line in lines:
    str = line.split()[0]
    lst = [int(c) for c in line.split()[1].split(",")]
    total += calc_line(str,tuple(lst))

print(total)

for line in lines:
    str = "?".join([line.split()[0]] * 5)
    lst = [int(c) for c in line.split()[1].split(",")] * 5
    total2 += calc_line(str,tuple(lst))

print(total2)