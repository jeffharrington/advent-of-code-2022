from day7a import calculate

test_input = [
    "$ cd /\n",
    "$ ls\n",
    "dir a\n",
    "14848514 b.txt\n",
    "8504156 c.dat\n",
    "dir d\n",
    "$ cd a\n",
    "$ ls\n",
    "dir e\n",
    "29116 f\n",
    "2557 g\n",
    "62596 h.lst\n",
    "$ cd e\n",
    "$ ls\n",
    "584 i\n",
    "$ cd ..\n",
    "$ cd ..\n",
    "$ cd d\n",
    "$ ls\n",
    "4060174 j\n",
    "8033020 d.log\n",
    "5626152 d.ext\n",
    "7214296 k\n",
]
answer = calculate(test_input)
expected_answer = 95437
assert answer == expected_answer, f"Answer ({answer}) != expected ({expected_answer})"
