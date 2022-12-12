#
# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12
#
from collections import deque


def calculate(lines: list[str]):
    matrix = []
    graph = {}
    start = (0, 0)
    end = (0, 0)
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(list(line.strip())):
            if char == "S":
                start = (i, j)
                row.append(ord("a"))
            elif char == "E":
                end = (i, j)
                row.append(ord("z"))
            else:
                row.append(ord(char))
        matrix.append(row)
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            neighbors = []
            curr_cord = (i, j)
            if i > 0:
                neighbor_coord = (i - 1, j)
                if valid_neighbor(matrix, start, curr_cord, neighbor_coord):
                    neighbors.append(neighbor_coord)
            if i < len(lines) - 1:
                neighbor_coord = (i + 1, j)
                if valid_neighbor(matrix, start, curr_cord, neighbor_coord):
                    neighbors.append(neighbor_coord)
            if j > 0:
                neighbor_coord = (i, j - 1)
                if valid_neighbor(matrix, start, curr_cord, neighbor_coord):
                    neighbors.append(neighbor_coord)
            if j < len(row) - 1:
                neighbor_coord = (i, j + 1)
                if valid_neighbor(matrix, start, curr_cord, neighbor_coord):
                    neighbors.append(neighbor_coord)
            graph[(i, j)] = neighbors
    distances, previous = dijkstra(graph, start)
    # print("-" * 25)
    # print(matrix)
    # print("-" * 25)
    # print(graph)
    # print("-" * 25)
    # print(distances)
    # print("-" * 25)
    # print(previous)
    return distances[end]


def valid_neighbor(matrix, start_coord, curr_coord, neighbor_coord) -> bool:
    if curr_coord == start_coord:
        # All neighbors of the start node are valid
        return True
    curr_val = matrix[curr_coord[0]][curr_coord[1]]
    neighbor_val = matrix[neighbor_coord[0]][neighbor_coord[1]]
    if (neighbor_val - 1) <= curr_val:
        # If the height of the neighbor is only 1 higher, it's valid
        return True
    return False


def dijkstra(graph, start):
    visited = set()  # (x, y) of visited nodes
    distances = {key: float("inf") for key in graph.keys()}
    previous = {key: None for key in graph.keys()}
    distances[start] = 0
    unvisited = deque()
    unvisited.append(start)
    while unvisited:
        curr = unvisited.popleft()
        curr_distance = distances[curr]
        visited.add(curr)
        unvisited_neighbors = [n for n in graph[curr] if n not in visited]
        for unvisited_neighbor in unvisited_neighbors:
            next_distance = curr_distance + 1
            if next_distance < distances[unvisited_neighbor]:
                distances[unvisited_neighbor] = next_distance
                previous[unvisited_neighbor] = curr
            unvisited.append(unvisited_neighbor)
    return distances, previous


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
