from part2 import calculate

test_input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

expected = 29
actual = calculate(test_input)
assert expected == actual, f"Answer ({actual}) != expected ({expected})"