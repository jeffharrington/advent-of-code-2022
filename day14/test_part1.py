from part1 import calculate

lines = [
    "498,4 -> 498,6 -> 496,6\n",
    "503,4 -> 502,4 -> 502,9 -> 494,9\n",
]


expected = 24
actual = calculate(lines)
assert expected == actual, f"Answer ({actual}) != expected ({expected})"
