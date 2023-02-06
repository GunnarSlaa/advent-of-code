def snafuToDec(snafu):
    return sum([snafuDict[char] * 5 ** i for i, char in enumerate(reversed(snafu))])


def decToSnafu(dec):
    for i in range(10000):
        if 5 ** i - 2 * 5 ** (i - 1) > dec:
            break
    result = ""
    for j in range(i):
        rest = ((dec % 5 ** (j + 1)) / 5 ** j)
        if rest > 2: rest -= 5
        result = decDict[rest] + result
        dec -= rest * 5 ** j
    return result


snafuDict = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

decDict = {value: key for key, value in snafuDict.items()}

with open("input", "r") as f:
    lines = f.read().split("\n")

print(decToSnafu(sum([snafuToDec(snafu) for snafu in lines])))