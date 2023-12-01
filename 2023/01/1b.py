import itertools
import re

with open("input", "r") as file:
    lines = file.read().strip().split("\n")

digit_dict = {"one": "1",
              "two": "2",
              "three": "3",
              "four": "4",
              "five": "5",
              "six": "6",
              "seven": "7",
              "eight": "8",
              "nine": "9"
              }

total = 0
for line in lines:
    digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    digits = [digit if digit.isdigit() else digit_dict[digit] for digit in digits]
    total += int("".join([digits[0], digits[-1]]))

print(total)