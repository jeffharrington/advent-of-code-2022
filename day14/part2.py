#
# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14
#
from typing import Tuple


def calculate(lines: list[str]):
    all_coords = set()
    grid = []

    # Get coordinates for all rocks
    for line in lines:
        points = [eval(coord) for coord in line.split(" -> ")]
        for i in range(1, len(points)):
            point1 = points[i - 1]
            point2 = points[i]
            coords = coordinates(point1, point2)
            all_coords.update(coords)

    min_col = min([col for col, row in all_coords])
    max_col = max([col for col, row in all_coords])

    min_row = min([row for col, row in all_coords])
    max_row = max([row for col, row in all_coords])

    # Shrink the width to make it easier to see
    reducer = min_col  # 494
    all_coords = [((col - reducer), row) for col, row in all_coords]

    min_col = min([col for col, row in all_coords])
    max_col = max([col for col, row in all_coords])

    min_row = min([row for col, row in all_coords])
    max_row = max([row for col, row in all_coords])

    print("Min Col:", min_col)
    print("Max Col:", max_col)

    print("Min Row:", min_row)
    print("Max Row:", max_row)

    print("reducer:", reducer)

    # Initialize Grid
    for i in range(max_row + 1):
        grid.append([])
        for j in range(max_col + 1):
            grid[i].append(".")

    # Fill in the rocks
    for rock in all_coords:
        grid[rock[1]][rock[0]] = "#"

    draw_grid(grid)

    starting_point = (500 - reducer, 0)
    overflowed = False
    print("Starting at:", starting_point)
    while not overflowed:
        curr_col, curr_row = starting_point
        grid[curr_row][curr_col] = "+"
        for _ in range(max_row + 1):
            print(f"Sand is at: {curr_row}, {curr_col}", grid[curr_row][curr_col])
            space_below = grid[curr_row + 1][curr_col]
            if space_below in ["#", "o"]:
                space_left = grid[curr_row + 1][curr_col - 1]
                if space_left in ["#", "o"]:
                    space_right = grid[curr_row + 1][curr_col + 1]
                    if space_right in ["#", "o"]:
                        grid[curr_row][curr_col] = "o"
                        break  # At rest!
                    else:
                        curr_col += 1  # Move right
                else:
                    curr_col -= 1  # Move Left
            curr_row += 1  # Advance
            if curr_row >= max_row:
                print("Overflown row!")
                overflowed = True
                break
            if curr_col >= max_col:
                print("Overflown col!")
                overflowed = True
                break
        draw_grid(grid)

    # Count the rocks at rest
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
