#
# Day 16: Proboscidea Volcanium
# https://adventofcode.com/2022/day/16
#
import re
from dataclasses import dataclass
from typing import List


FORMAT_PATTERN = re.compile(
    r"Valve (\w{2}) has flow rate=(\d*); tunnels? leads? to valves? (.*)$"
)


@dataclass
class Valve:
    name: str
    opened: bool
    rate: int
    connections: list


def calculate(lines: list[str]):
    valves = dict()
    for line in lines:
        name, rate, connections = FORMAT_PATTERN.match(line.strip()).groups()  # type: ignore
        valves[name] = Valve(
            name=name,
            opened=False,
            rate=int(rate),
            connections=connections.split(", "),
        )
    print(valves)
    result = search_valves(valves, "AA", 6, [], 0)
    print(result)


def search_valves(valves: dict, name: str, budget: int, path: list, score: int):
    if budget <= 0:
        return score, path
    else:
        valve = valves[name]
        path.append(name)
        score += valve.rate
        budget -= 1
        max_connection_score = 0
        best_path = None
        for connection in valve.connections:
            cscore, cpath = search_valves(
                valves.copy(), connection, budget, path.copy(), score
            )
            if cscore >= max_connection_score:
                best_path = (cscore, cpath)
        return best_path


# def search_valves(
#     valves: dict, turned_on: list, name: str, minute: int, score: int, path: list
# ):
#     valve = valves[name]
#     print(minute, valve.name, valve.opened, valve.rate, score, path)
#     if minute > 30:
#         return 0
#     path.append(name)
#     score += valve.rate
#     minute += 1
#     if valve.rate > 0 and not valve.opened and valve.name not in turned_on:
#         print("Opening valve:", valve.name)
#         valve.opened = True
#         path.append(f"open {valve.name}")
#         minute += 1
#     for connection in valve.connections:
#         search_valves(valves.copy(), turned_on, connection, minute, score, path.copy())
#     return 0


# def search_valves(valves: dict, name: str, step: int, pressure: int, path: list):
#     print("-" * 80)
#     valve = valves[name]
#     print(step, valve.name, valve.opened, valve.rate, valve.connections)
#     step -= 1
#     if step <= 0:
#         print("Returned!")
#         return pressure, path
#     for _, valve in valves.items():
#         if valve.opened:
#             pressure += valve.rate
#     if valve.rate > 0 and not valve.opened:
#         valve.opened = True
#         step -= 1
#     path.append(valve.name)
#     pressure_candidates = []
#     for connection in valve.connections:
#         if connection == path[-1]:
#             continue
#         pressure_candidates.append(
#             search_valves(valves, connection, step, pressure, path)
#         )
#     max_candidate = (0, 0)
#     for candidate in pressure_candidates:
#         if candidate[0] > max_candidate[0]:
#             max_candidate = candidate
#     print("Final return!")
#     return max_candidate


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
