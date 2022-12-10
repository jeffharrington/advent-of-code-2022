from day9a import calculate, move_to_touch

assert move_to_touch(head=[0, 0], tail=[0, 0]) == [0, 0]
assert move_to_touch(head=[1, 0], tail=[0, 0]) == [0, 0]
assert move_to_touch(head=[2, 0], tail=[1, 0]) == [0, 0]
assert move_to_touch(head=[3, 0], tail=[2, 0]) == [0, 0]
assert move_to_touch(head=[1, 3], tail=[2, 4]) == [0, 0]
assert move_to_touch(head=[2, 3], tail=[1, 1]) == [1, 1]

test_input = [
    "R 4\n",
    "U 4\n",
    "L 3\n",
    "D 1\n",
    "R 4\n",
    "D 1\n",
    "L 5\n",
    "R 2\n",
]

answer = calculate(test_input)
expected = 13
assert answer == expected, f"Answer ({answer}) != expected ({expected})"
