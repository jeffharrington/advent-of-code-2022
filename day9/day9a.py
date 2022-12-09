#
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
#
from typing import List

X = 0
Y = 1


def calculate(lines: list[str]):
    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_visits = set()
    for line in lines:
        direction, count_str = line.strip().split(" ")
        count = int(count_str)
        for i in range(count):
            match direction:
                case "R":
                    head_pos[X] += 1
                case "L":
                    head_pos[X] -= 1
                case "U":
                    head_pos[Y] += 1
                case "D":
                    head_pos[Y] -= 1
            move = move_to_touch(head_pos, tail_pos)
            tail_pos[X] += move[X]
            tail_pos[Y] += move[Y]
            tail_visits.add((tail_pos[X], tail_pos[Y]))
    return len(tail_visits)


def move_to_touch(head_pos: List[int], tail_pos: List[int]) -> List[int]:
    x_distance = head_pos[X] - tail_pos[X]
    y_distance = head_pos[Y] - tail_pos[Y]
    move = [0, 0]
    if x_distance > 1:
        move[X] += 1
        if y_distance >= 1:
            move[Y] += 1
        elif y_distance <= -1:
            move[Y] -= 1
    elif x_distance < -1:
        move[X] -= 1
        if y_distance >= 1:
            move[Y] += 1
        elif y_distance <= -1:
            move[Y] -= 1
    elif y_distance > 1:
        move[Y] += 1
        if x_distance >= 1:
            move[X] += 1
        elif x_distance <= -1:
            move[X] -= 1
    elif y_distance < -1:
        move[Y] -= 1
        if x_distance >= 1:
            move[X] += 1
        elif x_distance <= -1:
            move[X] -= 1
    return move


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
