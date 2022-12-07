#
# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7
#
import re
from typing import Dict
from collections import defaultdict

CD_PATTERN = re.compile(r"\$ cd (.*)")
FILE_PATTERN = re.compile(r"(\d+) (.*)")


def calculate(lines: list[str]):
    curr_path = []
    dir_size: Dict[str, int] = defaultdict(int)
    for line in lines:
        cmd = line.strip()
        if match := re.match(CD_PATTERN, cmd):
            match match.group(1):
                case "/":
                    curr_path = ["/"]
                case "..":
                    curr_path.pop()
                case _:
                    curr_path.append(match.group(1))
        elif match := re.match(FILE_PATTERN, cmd):
            file_size = match.group(1)
            for i in range(len(curr_path)):
                dir_key = "".join(curr_path[0 : len(curr_path) - i])
                dir_size[dir_key] += int(file_size)
    answer = sum([s for s in dir_size.values() if s <= 100000])
    return answer


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
