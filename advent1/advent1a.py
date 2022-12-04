#
# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1
#
def calculate(lines: list[str]):
    calorie_counts = [0]
    for line in lines:
        match line.strip():
            case "":
                calorie_counts.append(0)
            case _:
                calorie_counts[-1] += int(line)
    return max(calorie_counts)


with open("input.txt") as f:
    lines = f.readlines()

print(calculate(lines))
