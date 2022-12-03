#
# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3
#
import string


def calculate(lines: list[str]):
    SCORE_KEY = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    score = 0
    i = 0
    while i < len(lines):
        sack1 = set(lines[i].strip())
        sack2 = set(lines[i + 1].strip())
        sack3 = set(lines[i + 2].strip())
        common = (sack1 & sack2 & sack3).pop()
        score += SCORE_KEY.index(common) + 1
        i += 3
    return score


with open("input.txt") as f:
    lines = f.readlines()
print(calculate(lines))
