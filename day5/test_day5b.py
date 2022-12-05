from day5b import calculate

test_input = [
    "    [D]\n",
    "[N] [C]\n",
    "[Z] [M] [P]\n",
    " 1   2   3 \n",
    "\n",
    "move 1 from 2 to 1\n",
    "move 3 from 1 to 3\n",
    "move 2 from 2 to 1\n",
    "move 1 from 1 to 2\n",
]

answer = calculate(test_input)
expected_answer = "MCD"
assert answer == expected_answer, f"Answer ({answer}) != expected ({expected_answer})"
