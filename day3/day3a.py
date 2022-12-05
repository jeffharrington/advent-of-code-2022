#
# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3
#
import string


def calculate(lines: list[str]):
    SCORE_KEY = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    score = 0
    for line in lines:
        line = line.strip()
        halfway = len(line) // 2
        sack1 = set(line[0:halfway])
        sack2 = set(line[halfway:])
        misplaced = (sack1 & sack2).pop()
        score += SCORE_KEY.index(misplaced) + 1
    return score


with open("input.txt") as f:
    lines = f.readlines()
print(calculate(lines))
