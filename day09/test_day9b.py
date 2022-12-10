from day9b import calculate

test_input = [
    "R 5\n",
    "U 8\n",
    "L 8\n",
    "D 3\n",
    "R 17\n",
    "D 10\n",
    "L 25\n",
    "U 20\n",
]

answer = calculate(test_input)
expected = 36
assert answer == expected, f"Answer ({answer}) != expected ({expected})"
