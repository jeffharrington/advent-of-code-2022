#
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
#
from typing import List

X, Y = 0, 1


def calculate(lines: list[str]):
    head, tail = [0, 0], [0, 0]
    tail_visits = set()
    for line in lines:
        direction, count = line.strip().split(" ")
        for _ in range(int(count)):
            match direction:
                case "R":
                    head[X] += 1
                case "L":
                    head[X] -= 1
                case "U":
                    head[Y] += 1
                case "D":
                    head[Y] -= 1
            move = move_to_touch(head, tail)
            tail[X] += move[X]
            tail[Y] += move[Y]
            tail_visits.add((tail[X], tail[Y]))
    return len(tail_visits)


def move_to_touch(head: List[int], tail: List[int]) -> List[int]:
    """Return the move we need to make to make them touch (n, n)"""
    move = [0, 0]
    x_distance = head[X] - tail[X]
    y_distance = head[Y] - tail[Y]
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
