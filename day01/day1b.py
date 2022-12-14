#
# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1
#
def calculate(lines: list[str]):
    calorie_counts = [0]
    for line in lines:
        try:
            calorie_counts[-1] += int(line.strip())
        except ValueError:
            calorie_counts.append(0)
    calorie_counts.sort(reverse=True)
    return sum(calorie_counts[:3])


with open("input.txt") as f:
    lines = f.readlines()
print(calculate(lines))
