#
# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8
#
def calculate(lines: list[str]):
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))
    visible = 0
    last_row_index = len(matrix) - 1
    last_col_index = len(matrix[0]) - 1
    for row in range(len(matrix)):
        if row == 0 or row == last_row_index:
            visible += len(matrix[row])
            continue
        for col in range(len(matrix[row])):
            if col == 0 or col == last_col_index:
                visible += 1
            elif (
                visible_from_left(matrix, row, col)
                or visible_from_right(matrix, row, col)
                or visible_from_top(matrix, row, col)
                or visible_from_bottom(matrix, row, col)
            ):
                visible += 1
    return visible


def visible_from_top(matrix, row, col):
    target_val = matrix[row][col]
    col_vals = [matrix[i][col] for i in range(len(matrix))]
    for val in col_vals[:row]:
        if val >= target_val:
            return False
    return True


def visible_from_bottom(matrix, row, col):
    target_val = matrix[row][col]
    col_vals = [matrix[i][col] for i in range(len(matrix))]
    for val in col_vals[row + 1 :]:
        if val >= target_val:
            return False
    return True


def visible_from_left(matrix, row, col):
    target_val = matrix[row][col]
    for val in matrix[row][:col]:
        if val >= target_val:
            return False
    return True


def visible_from_right(matrix, row, col):
    target_val = matrix[row][col]
    for val in matrix[row][col + 1 :]:
        if val >= target_val:
            return False
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
