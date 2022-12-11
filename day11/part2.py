#
# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11
#
from math import lcm
from collections import deque
from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: deque
    operation: Callable
    divisor: int
    monkey_if_true: int
    monkey_if_false: int
    inspections: int


def calculate(lines: list[str], num_rounds=10000):
    monkeys: list[Monkey] = []
    for i in range(0, len(lines), 7):
        items = parse(lines[i + 1])
        operation = parse(lines[i + 2])
        test = parse(lines[i + 3])
        monkey_if_true = parse(lines[i + 4])
        monkey_if_false = parse(lines[i + 5])
        monkeys.append(
            Monkey(
                items=deque([int(s) for s in items.split(", ")]),
                operation=monkey_operation(operation),
                divisor=int(test.replace("divisible by ", "")),
                monkey_if_true=int(monkey_if_true.split(" ")[-1]),
                monkey_if_false=int(monkey_if_false.split(" ")[-1]),
                inspections=0,
            )
        )
    lowest_common_multiple = lcm(*[m.divisor for m in monkeys])
    for _ in range(num_rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                high_worry = monkey.operation(item)
                low_worry = high_worry % lowest_common_multiple
                if low_worry % monkey.divisor == 0:
                    new_monkey = monkey.monkey_if_true
                else:
                    new_monkey = monkey.monkey_if_false
                monkeys[new_monkey].items.append(low_worry)
                monkey.inspections += 1
    ordered_inspections = sorted([monkey.inspections for monkey in monkeys])
    return ordered_inspections[-1] * ordered_inspections[-2]


def parse(s: str) -> str:
    return s.strip().split(": ")[1]


def monkey_operation(operation: str) -> Callable:
    match operation.split(" = ")[1].split(" "):
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


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
