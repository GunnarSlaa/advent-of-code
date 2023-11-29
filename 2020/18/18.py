from grid_utils import *

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

lines = ["".join(line.split()) for line in lines]


def find_parenth(string, index):
    begin = index
    index += 1
    parenth = 1
    while parenth > 0:
        if string[index] == '(':
            parenth += 1
        elif string[index] == ')':
            parenth -= 1
        index += 1
    return string[begin + 1: index - 1], index


def calc(input):
    if input[0].isdigit():
        value = int(input[0])
        i = 1
    else:
        value = calc(find_parenth(input, 0)[0])
        i = find_parenth(input, 0)[1]
    while i < len(input):
        char = input[i]
        if char in ['*', '+']:
            operator = char
            i += 1
        elif char.isdigit():
            if operator == '*':
                value *= int(char)
            elif operator == '+':
                value += int(char)
            i += 1
        elif char == '(':
            if operator == '*':
                value *= calc(find_parenth(input, i)[0])
            elif operator == '+':
                value += calc(find_parenth(input, i)[0])
            i = find_parenth(input, i)[1]
    return value


print(sum([calc(line) for line in lines]))
