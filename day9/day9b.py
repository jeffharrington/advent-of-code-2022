#
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
#
from typing import List

X, Y = 0, 1


def calculate(lines: list[str], num_knots=10):
    knots = []
    tail_visits = set()
    for _ in range(num_knots):
        knots.append([0, 0])
    final_tail_index = num_knots - 1
    for line in lines:
        direction, count = line.strip().split(" ")
        for i in range(int(count)):
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
                next_index = knot_index + 1
                move = move_to_touch(knots[knot_index], knots[next_index])
                knots[next_index][X] += move[X]
                knots[next_index][Y] += move[Y]
                tail_visits.add(
                    (knots[final_tail_index][X], knots[final_tail_index][Y])
                )
    return len(tail_visits)


def move_to_touch(head_pos: List[int], tail_pos: List[int]) -> List[int]:
    """Return the move we need to make to make them touch (n, n)"""
    x_distance = head_pos[X] - tail_pos[X]
    y_distance = head_pos[Y] - tail_pos[Y]
    max_distance = max(abs(x_distance), abs(y_distance))
    move = [0, 0]
    if max_distance > 1:
        move[X] += distance_to_move(x_distance)
        move[Y] += distance_to_move(y_distance)
    return move


def distance_to_move(distance: int) -> int:
    """Return the distance (either positive or negative) to move for specified distance"""
    if distance >= 1:
        return 1
    elif distance <= -1:
        return -1
    else:
        return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
