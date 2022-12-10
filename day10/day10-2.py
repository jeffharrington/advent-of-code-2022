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
        report(register, cycle)
        instruction = stack.popleft()
        match instruction:
            case ["addx", num]:
                stack.appendleft(["add", num])
            case ["add", num]:
                register += int(num)
        cycle += 1


def report(register, cycle):
    x = (cycle % 40) - 1
    sprite = (register - 1, register, register + 1)
    if x == 0:
        print("")  # Newline
    if x in sprite:
        print("#", end="")
    else:
        print(".", end="")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
