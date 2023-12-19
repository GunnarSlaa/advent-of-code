from functools import reduce
from copy import deepcopy

with open("input", "r") as file:
    blocks = file.read().strip().split("\n\n")

workflows = {}
for workflow in blocks[0].split("\n"):
    workflows[workflow.split("{")[0]] = workflow.split("{")[1].split("}")[0]


def calc_range(ranges, wf):
    if wf == "A":
        return reduce((lambda x, y: x * y), [r[1] - r[0] + 1 for r in ranges.values()])
    elif wf == "R":
        return 0
    elif ":" not in wf:
        return calc_range(ranges, workflows[wf])
    else:
        match_range = deepcopy(ranges)
        no_match_range = deepcopy(ranges)
        if "<" in wf[:2]:
            letter = wf.split("<")[0]
            edge = int(wf.split("<")[1].split(":")[0])
            if ranges[letter][1] < edge:
                return calc_range(match_range, wf.split(",")[0].split(":")[1])
            elif ranges[letter][0] < edge < ranges[letter][1]:
                match_range[letter] = (match_range[letter][0], edge - 1)
                no_match_range[letter] = (edge, no_match_range[letter][1])
                match_outcome = calc_range(match_range, wf.split(",")[0].split(":")[1])
                no_match_outcome = calc_range(no_match_range, wf.split(",", 1)[1])
                return match_outcome + no_match_outcome
            elif ranges[letter][0] >= edge:
                return calc_range(no_match_range, wf.split(",", 1)[1])
        elif ">" in wf[:2]:
            letter = wf.split(">")[0]
            edge = int(wf.split(">")[1].split(":")[0])
            if ranges[letter][0] > edge:
                return calc_range(match_range, wf.split(",")[0].split(":")[1])
            elif ranges[letter][0] < edge < ranges[letter][1]:
                match_range[letter] = (edge + 1, match_range[letter][1])
                no_match_range[letter] = (no_match_range[letter][0], edge)
                match_outcome = calc_range(match_range, wf.split(",")[0].split(":")[1])
                no_match_outcome = calc_range(no_match_range, wf.split(",", 1)[1])
                return match_outcome + no_match_outcome
            elif ranges[letter][1] <= edge:
                return calc_range(no_match_range, wf.split(",", 1)[1])
        match_outcome = calc_range(match_range, wf.split(",")[0].split(":")[1])
        no_match_outcome = calc_range(no_match_range, wf.split(",", 1)[1])
        return match_outcome + no_match_outcome


ranges = {"x": (1,4000),
          "m": (1,4000),
          "a": (1,4000),
          "s": (1,4000)}
print(calc_range(ranges, workflows["in"]))
