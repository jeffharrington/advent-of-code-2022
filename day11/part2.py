#
# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11
#
import re
from collections import deque, defaultdict
from typing import Callable, Dict

MONKEY_PATTERN = re.compile(r"Monkey (\d+):")
STARTING_ITEMS_PATTERN = re.compile(r"  Starting items: (.*)$")
OPERATION_PATTERN = re.compile(r"  Operation: (.*)$")
TEST_PATTERN = re.compile(r"  Test: (.*)$")
IF_TRUE_PATTERN = re.compile(r"    If true: (.*)$")
IF_FALSE_PATTERN = re.compile(r"    If false: (.*)$")


def calculate(lines: list[str], num_rounds=10000):
    monkeys: list[Dict] = []
    for i in range(0, len(lines), 7):
        monkey_index = int(MONKEY_PATTERN.match(lines[i])[1])
        items_str = STARTING_ITEMS_PATTERN.match(lines[i + 1])[1].split(", ")
        operation_str = OPERATION_PATTERN.match(lines[i + 2])[1]
        test_str = TEST_PATTERN.match(lines[i + 3])[1]
        monkey_if_true = IF_TRUE_PATTERN.match(lines[i + 4])[1]
        monkey_if_false = IF_FALSE_PATTERN.match(lines[i + 5])[1]
        monkeys.append(
            dict(
                index=monkey_index,
                items=deque([int(s) for s in items_str]),
                operation=monkey_operation(operation_str),
                test=monkey_test(test_str),
                monkey_if_true=int(monkey_if_true.split(" ")[-1]),
                monkey_if_false=int(monkey_if_false.split(" ")[-1]),
            )
        )
    inspections: Dict[int, int] = defaultdict(int)
    for i in range(num_rounds):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].popleft()
                inspections[monkey["index"]] += 1
                new_worry = monkey["operation"](item)
                print("Worry level now:", new_worry)
                if monkey["test"](new_worry):
                    new_monkey = monkey["monkey_if_true"]
                else:
                    new_monkey = monkey["monkey_if_false"]
                monkeys[new_monkey]["items"].append(new_worry)
    ordered_inspections = sorted(inspections.values())
    return ordered_inspections[-1] * ordered_inspections[-2]


def monkey_operation(operation_str: str) -> Callable:
    operands = operation_str.split(" = ")[1].split(" ")
    match operands:
        case [n1, "+", n2]:
            if n1 == "old" and n2 == "old":
                return lambda n: n + n
            elif n1 == "old":
                return lambda n: n + int(n2)
            elif n2 == "old":
                return lambda n: n + int(n1)
        case [n1, "*", n2]:
            if n1 == "old" and n2 == "old":
                return lambda n: n * n
            elif n1 == "old":
                return lambda n: n * int(n2)
            elif n2 == "old":
                return lambda n: n * int(n1)
    return lambda n: n


def monkey_test(test_str: str) -> Callable:
    operands = test_str.split(" ")
    match operands:
        case ["divisible", "by", divisor]:
            return lambda n: n % int(divisor) == 0
    return lambda n: n


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
