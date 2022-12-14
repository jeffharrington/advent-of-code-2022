from part2 import compare_lists


left = [1, 1, 3, 1, 1]
right = [1, 1, 5, 1, 1]
actual = compare_lists(left, right)
expected = -1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1]
right = [1]
actual = compare_lists(left, right)
expected = 0
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1]
right = [2]
actual = compare_lists(left, right)
expected = -1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [2]
right = [1]
actual = compare_lists(left, right)
expected = 1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1, 1]
right = [1, 2]
actual = compare_lists(left, right)
expected = -1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [[[]]]
right = [[]]
actual = compare_lists(left, right)
expected = 1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [[1], [2, 3, 4]]
right = [[1], 4]
actual = compare_lists(left, right)
expected = -1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"


left = [[4, 4], 4, 4]
right = [[4, 4], 4, 4, 4]
actual = compare_lists(left, right)
expected = -1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [[1], 4]
right = [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
actual = compare_lists(left, right)
expected = 1
assert expected == actual, f"Answer ({actual}) != expected ({expected})"
