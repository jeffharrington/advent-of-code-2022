#
# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4
#
def calculate(lines: list[str]):
    score = 0
    for line in lines:
        e1_start, e1_end, e2_start, e2_end = [
            int(section)
            for elf in line.strip().split(",")
            for section in elf.split("-")
        ]
        score += int(
            (e2_start <= e1_start and e2_end >= e1_end)
            or (e1_start <= e2_start and e1_end >= e2_end)
        )
    return score


match __name__:
    case "__main__":
        with open("input.txt") as f:
            lines = f.readlines()
        print(calculate(lines))
