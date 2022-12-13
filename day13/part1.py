#
# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13
#
from typing import Optional


def calculate(lines: list[str]):
    correct_sum = 0
    for i in range(0, len(lines), 3):
        left_list = eval(lines[i].strip())
        right_list = eval(lines[i + 1].strip())
        correct_order = compare_lists(left_list, right_list)
        print(left_list, "vs", right_list, correct_order)
        if correct_order:
            correct_sum += (i // 3) + 1
    return correct_sum


def compare_lists(left, right) -> Optional[bool]:
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    len_left = len(left)
    len_right = len(right)
    for i in range(max(len_left, len_right)):
        if i >= len_left and i < len_right:
            return True
        elif i >= len_right and i < len_left:
            return False
        lval = left[i]
        rval = right[i]
        if isinstance(lval, list) or isinstance(rval, list):
            sub_result = compare_lists(lval, rval)
            if sub_result is None:
                continue
            else:
                return sub_result
        elif lval < rval:
            return True
        elif lval > rval:
            return False
        else:
            continue
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
