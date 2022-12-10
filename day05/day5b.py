#
# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5
#
import re
from collections import defaultdict
from typing import Dict

CRATE_LENGTH = 3
NUMBER_PATTERN = re.compile(r"(\s+\d)+\n")
CRATE_PATTERN = re.compile(r"(\[\w\]\s)|((   \s))")
MOVE_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")


def calculate(lines: list[str]):
    stacks: Dict[int, list] = defaultdict(list)
    for line in lines:
        if matches := re.findall(CRATE_PATTERN, line):
            stack_num = 0
            for match in matches:
                match letter := match[0].strip().replace("[", "").replace("]", ""):
                    case "":
                        pass
                    case _:
                        stacks[stack_num].insert(0, letter)
                stack_num += 1
        elif move := re.match(MOVE_PATTERN, line):
            num_crates = int(move[1])
            source = int(move[2]) - 1
            dest = int(move[3]) - 1
            stack_move: list[str] = []
            for i in range(num_crates):
                crate = stacks[source].pop()
                stack_move.insert(0, crate)
            stacks[dest].extend(stack_move)
    return "".join([stacks[i][-1] for i in range(len(stacks))])


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
