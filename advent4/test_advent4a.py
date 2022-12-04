from advent4a import calculate


test_input = [
    "2-4,6-8\n",
    "2-3,4-5\n",
    "5-7,7-9\n",
    "2-8,3-7\n",
    "6-6,4-6\n",
    "2-6,4-8\n",
]
score = calculate(lines=test_input)
expected_score = 2
assert score == expected_score, f"Score ({score}) != expected ({expected_score})"
