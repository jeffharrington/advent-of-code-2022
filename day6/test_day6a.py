from day6a import calculate

test_input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb\n"]
answer = calculate(test_input)
expected_answer = 7
assert answer == expected_answer, f"Answer ({answer}) != expected ({expected_answer})"
