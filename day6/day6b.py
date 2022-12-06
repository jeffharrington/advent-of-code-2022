#
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
#
MARKER_LENGTH = 14


def calculate(lines: list[str]):
    line = list(lines[0])
    i = 0
    while len(set(line[i : (i + MARKER_LENGTH)])) != MARKER_LENGTH:
        i += 1
    return i + MARKER_LENGTH


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
