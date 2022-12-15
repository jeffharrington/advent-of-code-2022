#
# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14
#
from typing import Tuple


def calculate(lines: list[str]):
    all_coords = set()
    grid = []
    for line in lines:
        points = [eval(coord) for coord in line.split(" -> ")]
        # print(points)
        for i in range(1, len(points)):
            point1 = points[i - 1]
            point2 = points[i]
            coords = coordinates(point1, point2)
            # print("Line is:", coords)
            all_coords.update(coords)
    # min_col = min([col for col, row in all_coords])
    # all_coords = [(col - min_col, row) for col, row in all_coords]
    reducer = min([col for col, row in all_coords])
    all_coords = [((col - reducer), row) for col, row in all_coords]

    max_col = max([col for col, row in all_coords])
    max_row = max([row for col, row in all_coords])
    print("max_col:", max_col)
    print("max_row:", max_row)

    min_col = min([col for col, row in all_coords])
    min_row = min([row for col, row in all_coords])
    print("min_col:", min_col)
    print("min_row:", min_row)

    # Initialize Grid
    for i in range(max_row + 1):
        grid.append([])
        for j in range(max_col + 1):
            grid[i].append(".")
    print("Rows:", len(grid))
    print("Cols:", len(grid[0]))

    # Add rocks
    for rock in all_coords:
        # print("Rock at:", rock[0], ",", rock[1])
        grid[rock[1]][rock[0]] = "#"

    # Stream sand
    starting_point = (500 - reducer, 0)
    print("Starting point is:", starting_point)
    overflowed = False
    while not overflowed:
        # print("*" * 100)
        # print("Max Row:", max_row)
        # print("Max Col:", max_col)
        rock_col, rock_row = starting_point
        for curr_row in range(max_row + 1):
            if curr_row >= max_row:
                overflowed = True
                break
            if rock_col - 1 < 0:
                overflowed = True
                break
            if rock_col + 1 >= max_col:
                overflowed = True
                break
            # print(f"Curr {curr_row}, {rock_col}:", grid[curr_row][rock_col])
            # print(f"Below {curr_row + 1}, {rock_col}:", space_below)
            space_below = grid[curr_row + 1][rock_col]
            space_left = grid[curr_row + 1][rock_col - 1]
            space_right = grid[curr_row + 1][rock_col + 1]
            # print(f"Left {curr_row + 1}, {rock_col - 1}:", space_left)
            # print(f"Right {curr_row + 1}, {rock_col + 1}:", space_right)
            if space_below in ["#", "o"]:
                if space_left in ["#", "o"]:
                    if space_right in ["#", "o"]:
                        grid[curr_row][rock_col] = "o"
                        break
                    else:
                        rock_col += 1
                else:
                    rock_col -= 1
    draw_grid(grid)

    num_rocks = 0
    for row in grid:
        for col in row:
            if col == "o":
                num_rocks += 1
    return num_rocks


def draw_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")


def coordinates(coord1, coord2) -> list[Tuple[int, int]]:
    x1, y1 = coord1  # 498, 4
    x2, y2 = coord2  # 498, 6
    coords = []
    if x1 == x2:  # Moving vertically
        lower = min(y1, y2)
        higher = max(y1, y2)
        for i in range(lower, higher + 1):
            coords.append((x1, i))
    elif y1 == y2:
        lower = min(x1, x2)
        higher = max(x1, x2)
        for i in range(lower, higher + 1):
            coords.append((i, y1))
    return coords


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
