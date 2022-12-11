#
# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11
#
from collections import deque
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: deque
    operation: Callable
    test: Callable
    monkey_if_true: int
    monkey_if_false: int
    inspections: int


def calculate(lines: list[str], num_rounds=20):
    monkeys: list[Monkey] = []
    for i in range(0, len(lines), 7):
        items_str = parse_val(lines[i + 1])
        operation_str = parse_val(lines[i + 2])
        test_str = parse_val(lines[i + 3])
        monkey_if_true = parse_val(lines[i + 4])
        monkey_if_false = parse_val(lines[i + 5])
        monkeys.append(
            Monkey(
                items=deque([int(s) for s in items_str.split(", ")]),
                operation=monkey_operation(operation_str),
                test=monkey_test(test_str),
                monkey_if_true=int(monkey_if_true.split(" ")[-1]),
                monkey_if_false=int(monkey_if_false.split(" ")[-1]),
                inspections=0,
            )
        )
    for _ in range(num_rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                high_worry = monkey.operation(item)
                low_worry = high_worry // 3
                if monkey.test(low_worry):
                    new_monkey = monkey.monkey_if_true
                else:
                    new_monkey = monkey.monkey_if_false
                monkeys[new_monkey].items.append(low_worry)
                monkey.inspections += 1
    ordered_inspections = sorted([monkey.inspections for monkey in monkeys])
    return ordered_inspections[-1] * ordered_inspections[-2]


def parse_val(s: str) -> str:
    return s.strip().split(": ")[1]


def monkey_operation(operation_str: str) -> Callable:
    match operation_str.split(" = ")[1].split(" "):
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
    match test_str.split(" "):
        case ["divisible", "by", divisor]:
            return lambda n: n % int(divisor) == 0
    return lambda n: n


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
