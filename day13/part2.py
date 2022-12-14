#
# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13
#
from functools import cmp_to_key


def calculate(lines: list[str]):
    lists = []
    for line in lines:
        if stripped_line := line.strip():
            lists.append(eval(stripped_line))
    lists.append([[2]])
    lists.append([[6]])
    sorted_list = sorted(lists, key=cmp_to_key(compare_lists))
    decoder1 = sorted_list.index([[2]]) + 1
    decoder2 = sorted_list.index([[6]]) + 1
    return decoder1 * decoder2


def compare_lists(left, right) -> int:
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    len_left = len(left)
    len_right = len(right)
    for i in range(max(len_left, len_right)):
        if i >= len_left and i < len_right:
            return -1
        elif i >= len_right and i < len_left:
            return 1
        lval = left[i]
        rval = right[i]
        if isinstance(lval, list) or isinstance(rval, list):
            sub_result = compare_lists(lval, rval)
            if sub_result == 0:
                continue
            else:
                return sub_result
        elif lval < rval:
            return -1
        elif lval > rval:
            return 1
        else:
            continue
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
