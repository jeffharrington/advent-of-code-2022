#
# Day 15: Beacon Exclusion Zone
# https://adventofcode.com/2022/day/15
#
import re

TARGET_ROW = 2_000_000
SENSOR_PATTERN = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)


def calculate(lines: list[str]):
    min_col, max_col, max_distance = 0, 0, 0
    sensor_map = dict()
    beacons = set()
    for line in lines:
        m = SENSOR_PATTERN.match(line.strip())
        sensor = (int(m[1]), int(m[2]))  # x,y
        beacon = (int(m[3]), int(m[4]))  # x,y
        beacon_distance = distance(sensor, beacon)
        sensor_map[sensor] = (beacon, beacon_distance)
        beacons.add(beacon)
        max_distance = max(beacon_distance, max_distance)
        min_col = min([min_col, sensor[0], beacon[0]])
        max_col = max([max_col, sensor[0], beacon[0]])

    spaces_to_check = []
    for i in range(min_col - max_distance - 1, max_col + 1 + max_distance):
        spaces_to_check.append((i, TARGET_ROW))

    free_spaces = set()
    for sensor, (beacon, beacon_distance) in sensor_map.items():
        x = sensor[1]
        if (x - beacon_distance) > TARGET_ROW > (x + beacon_distance):
            # Skip!
            continue
        print("Sensor:", sensor, ", Beacon:", beacon, ", Distance:", beacon_distance)
        for space in spaces_to_check:
            space_distance = distance(space, sensor)
            if space_distance <= beacon_distance and is_free(
                space, beacons, sensor_map.keys()
            ):
                free_spaces.add(space)
    return len(free_spaces)


def is_free(coord, beacons, sensors):
    return coord not in beacons and coord not in sensors


def distance(pa, pb) -> int:
    return abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    print(calculate(lines))
