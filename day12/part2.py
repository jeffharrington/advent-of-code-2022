#
# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12
#
from collections import deque

START = "S"
END = "E"


def calculate(lines: list[str]):
    matrix = []
    graph = {}
    starts = []
    end = (0, 0)
    # Build matrix
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(list(line.strip())):
            if char == START:
                starts.append((i, j))
                row.append(ord("a"))
            elif char == END:
                end = (i, j)
                row.append(ord("z"))
            elif char == "a":
                starts.append((i, j))
                row.append(ord(char))
            else:
                row.append(ord(char))
        matrix.append(row)
    # Build graph
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            neighbors = []
            curr = (i, j)
            if i > 0:
                top_neighbor = (i - 1, j)
                if valid_neighbor(matrix, curr, top_neighbor):
                    neighbors.append(top_neighbor)
            if i < len(lines) - 1:
                bottom_neighbor = (i + 1, j)
                if valid_neighbor(matrix, curr, bottom_neighbor):
                    neighbors.append(bottom_neighbor)
            if j > 0:
                left_neighbor = (i, j - 1)
                if valid_neighbor(matrix, curr, left_neighbor):
                    neighbors.append(left_neighbor)
            if j < len(row) - 1:
                right_neighbor = (i, j + 1)
                if valid_neighbor(matrix, curr, right_neighbor):
                    neighbors.append(right_neighbor)
            graph[(i, j)] = neighbors
    shortest_distance = float("inf")
    for start in starts:
        distances, _ = dijkstra(graph, start)
        shortest_distance = min(shortest_distance, distances[end])
    return shortest_distance


def valid_neighbor(matrix, curr, neighbor) -> bool:
    curr_val = matrix[curr[0]][curr[1]]
    neighbor_val = matrix[neighbor[0]][neighbor[1]]
    if (neighbor_val - 1) <= curr_val:
        # If the height of the neighbor is only 1 higher, it's valid
        return True
    return False


def dijkstra(graph, start):
    visited = set()
    distances = {key: float("inf") for key in graph.keys()}
    previous = {key: None for key in graph.keys()}
    distances[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        curr_distance = distances[curr]
        visited.add(curr)
        unvisited_neighbors = [n for n in graph[curr] if n not in visited]
        for unvisited_neighbor in unvisited_neighbors:
            next_distance = curr_distance + 1
            if next_distance <= distances[unvisited_neighbor]:
                distances[unvisited_neighbor] = next_distance
                previous[unvisited_neighbor] = curr
            queue.append(unvisited_neighbor)
    return distances, previous


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
