#
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
#
def calculate(lines: list[str]):
    register = 1
    cycle = 1
    strength = 0
    for line in lines:
        instruction = line.strip().split(" ")
        match instruction:
            case ["noop"]:
                cycle, strength = tick(cycle, register, strength)
            case ["addx", num]:
                for i in range(2):
                    cycle, strength = tick(cycle, register, strength)
                register += int(num)
    return strength


def tick(cycle, register, strength):
    CYCLE_REPORTS = [20, 60, 100, 140, 180, 220]
    if cycle in CYCLE_REPORTS:
        strength += cycle * register
    return cycle + 1, strength


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
