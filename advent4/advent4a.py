#
# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4
#
def calculate(lines: list[str]):
    score = 0
    for line in lines:
        e1_beg, e1_end, e2_beg, e2_end = [
            int(section)
            for elf in line.strip().split(",")
            for section in elf.split("-")
        ]
        if (e2_beg <= e1_beg and e2_end >= e1_end) or (
            e1_beg <= e2_beg and e1_end >= e2_end
        ):
            score += 1
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))