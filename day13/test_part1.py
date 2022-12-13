from part1 import compare_lists


left = [1, 1, 3, 1, 1]
right = [1, 1, 5, 1, 1]
actual = compare_lists(left, right)
expected = True
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1]
right = [1]
actual = compare_lists(left, right)
expected = None
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1]
right = [2]
actual = compare_lists(left, right)
expected = True
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [2]
right = [1]
actual = compare_lists(left, right)
expected = False
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [1, 1]
right = [1, 2]
actual = compare_lists(left, right)
expected = True
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [[[]]]
right = [[]]
actual = compare_lists(left, right)
expected = False
assert expected == actual, f"Answer ({actual}) != expected ({expected})"

left = [[1], [2, 3, 4]]
right = [[1], 4]
actual = compare_lists(left, right)
expected = True
assert expected == actual, f"Answer ({actual}) != expected ({expected})"


left = [[4, 4], 4, 4]
right = [[4, 4], 4, 4, 4]
actual = compare_lists(left, right)
expected = True
assert expected == actual, f"Answer ({actual}) != expected ({expected})"
