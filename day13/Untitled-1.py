#
# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13
#
from collections import deque


def calculate(lines: list[str]):
    lq = deque()
    rq = deque()
    lstack = []
    rstack = []
    for i in range(0, len(lines), 3):
        left_queue = deque(eval(lines[i].strip()))
        right_queue = deque(eval(lines[i + 1].strip()))
        print("-" * 80)
        print("left_queue:", left_queue)
        print("right_queue:", right_queue)
        left = left_queue.popleft() if left_queue else None
        right = right_queue.popleft() if right_queue else None
        while left is not None and right is not None:
            pass
    return


def compare_lists(left, right) -> bool:
    for l, r in zip(left, right):
        if not left:
            return True
        if not right:
            return False
        if left < right:
            return True
        elif left > right:
            return False
        else:
            continue


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
