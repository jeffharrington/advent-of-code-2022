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
            for curr in range(num_knots - 1):
                next = curr + 1
                move = move_to_touch(knots[curr], knots[next])
                knots[next][X] += move[X]
                knots[next][Y] += move[Y]
            tail_visits.add((knots[-1][X], knots[-1][Y]))
    return len(tail_visits)


def move_to_touch(head_pos: List[int], tail_pos: List[int]) -> List[int]:
    """Return the move we need to make to make them touch (n, n)"""
    move = [0, 0]
    x_distance = head_pos[X] - tail_pos[X]
    y_distance = head_pos[Y] - tail_pos[Y]
    max_distance = max(abs(x_distance), abs(y_distance))
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
