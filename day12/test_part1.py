from part1 import calculate

test_input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

expected = 31
actual = calculate(test_input)
assert expected == actual, f"Answer ({actual}) != expected ({expected})"