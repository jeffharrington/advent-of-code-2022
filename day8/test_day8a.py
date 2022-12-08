from day8a import calculate

test_input = [
    "30373\n",
    "25512\n",
    "65332\n",
    "33549\n",
    "35390\n",
]
answer = calculate(test_input)
expected_answer = 21
assert answer == expected_answer, f"Answer ({answer}) != expected ({expected_answer})"
