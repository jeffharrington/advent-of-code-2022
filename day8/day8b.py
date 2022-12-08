#
# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8
#


def calculate(lines: list[str]):
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))
    scenic_scores = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            left_score = score_from_left(matrix, row, col)
            right_score = score_from_right(matrix, row, col)
            top_score = score_from_top(matrix, row, col)
            bottom_score = score_from_bottom(matrix, row, col)
            scenic_score = left_score * right_score * top_score * bottom_score
            scenic_scores.append(scenic_score)
    return max(scenic_scores)


def score_from_top(matrix, row, col):
    target_val = matrix[row][col]
    col_vals = [matrix[i][col] for i in range(len(matrix))]
    score = 0
    top_vals = col_vals[:row]
    top_vals.reverse()
    for val in top_vals:
        if val < target_val:
            score += 1
        elif val >= target_val:
            score += 1
            return score
    return score


def score_from_bottom(matrix, row, col):
    target_val = matrix[row][col]
    col_vals = [matrix[i][col] for i in range(len(matrix))]
    score = 0
    for val in col_vals[row + 1 :]:
        if val < target_val:
            score += 1
        elif val >= target_val:
            score += 1
            return score
    return score


def score_from_left(matrix, row, col):
    target_val = matrix[row][col]
    score = 0
    left_vals = matrix[row][:col]
    left_vals.reverse()
    for val in left_vals:
        if val < target_val:
            score += 1
        elif val >= target_val:
            score += 1
            return score
    return score


def score_from_right(matrix, row, col):
    target_val = matrix[row][col]
    score = 0
    for val in matrix[row][col + 1 :]:
        if val < target_val:
            score += 1
        elif val >= target_val:
            score += 1
            return score
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
