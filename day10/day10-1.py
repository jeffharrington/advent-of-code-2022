#
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
#
def calculate(commands: list[str]):
    register = 1
    cycle = 1
    strength = 0
    for command in commands:
        match command.strip().split(" "):
            case ["noop"]:
                cycle, strength = tick(cycle, register, strength)
            case ["addx", num]:
                for i in range(2):
                    cycle, strength = tick(cycle, register, strength)
                register += int(num)
    return strength


def tick(cycle, register, strength):
    if cycle in [20, 60, 100, 140, 180, 220]:
        strength += cycle * register
    return cycle + 1, strength


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
