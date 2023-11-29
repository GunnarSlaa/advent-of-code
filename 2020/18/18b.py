from grid_utils import *
import re
from functools import reduce

with open("input_test", "r") as file:
    lines = file.read().strip().split("\n")

lines = [line.replace(" ", "") for line in lines]


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


def calc2(inp):
    while '(' in inp:
        index = inp.find('(')
        inp = inp[:index] + str(calc2(find_parenth(inp, index)[0])) + inp[find_parenth(inp, index)[1]:]
    while '+' in inp:
        p = re.findall("[0-9]+\+[0-9]+", inp)
        inp = inp.replace(p[0], str(sum([int(c) for c in p[0].split("+")])), 1)
    return reduce((lambda x, y: x * y), [int(c) for c in inp.split("*")])

print(sum([calc2(line) for line in lines]))