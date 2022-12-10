#
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
#
from collections import deque


def calculate(lines: list[str]):
    register = 1
    cycle = 1
    stack: deque = deque()
    for line in lines:
        stack.append(line.strip().split(" "))
    while stack:
        instruction = stack.popleft()
        report(register, cycle)
        match instruction:
            case ["noop"]:
                pass
            case ["addx", num]:
                stack.appendleft(["add", num])
            case ["add", num]:
                register += int(num)
        cycle += 1


def report(register, cycle):
    sprite = (register - 1, register, register + 1)
    x = (cycle % 40) - 1
    if x == 0:
        print("")
    if x in sprite:
        print("#", end="")
    else:
        print(".", end="")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
