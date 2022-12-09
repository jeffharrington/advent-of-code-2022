#
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
#
from typing import List

X = 0
Y = 1


def calculate(lines: list[str], num_knots=10):
    knots = []
    for _ in range(num_knots):
        knots.append([0, 0])
    tail_visits = set()
    final_tail_index = num_knots - 1
    for line in lines:
        direction, count_str = line.strip().split(" ")
        count = int(count_str)
        for i in range(count):
            match direction:
                case "R":
                    knots[0][X] += 1
                case "L":
                    knots[0][X] -= 1
                case "U":
                    knots[0][Y] += 1
                case "D":
                    knots[0][Y] -= 1
            for knot_index in range(num_knots):
                if knot_index == final_tail_index:
                    continue
                curr_index = knot_index
                next_index = knot_index + 1
                move = move_to_touch(knots[curr_index], knots[next_index])
                knots[next_index][X] += move[X]
                knots[next_index][Y] += move[Y]
                tail_visits.add(
                    (knots[final_tail_index][X], knots[final_tail_index][Y])
                )
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
