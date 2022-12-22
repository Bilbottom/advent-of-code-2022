"""
OOP solution for day 15.
"""

from __future__ import annotations

from typing import Any


# noinspection DuplicatedCode
class Position(tuple):
    """
    A position on a 2-dimensional plane of integers.

    Note: this violates the Liskov Substitution Principle. This should inherit
    from some other class, try checking:

    - https://docs.python.org/3/library/collections.abc.html
    """
    def __new__(cls, *args):
        return super(Position, cls).__new__(cls, args)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def __add__(self, other: Position | tuple[int, ]):
        other = Position.from_tuple(other) if isinstance(other, tuple) else other
        length = max(len(self), len(other))

        return Position(
            *(self.get(index_) + other.get(index_) for index_ in range(length))
        )

    def __radd__(self, other: Position | tuple[int, ]):
        return self.__add__(other)

    def __iadd__(self, other: Position | tuple[int, ]):
        return self.__add__(other)

    def __sub__(self, other):
        other = Position.from_tuple(other) if isinstance(other, tuple) else other
        length = max(len(self), len(other))

        return Position(
            *(self.get(index_) - other.get(index_) for index_ in range(length))
        )

    def __rsub__(self, other: Position | tuple[int, ]):
        return self.__sub__(other)

    def __isub__(self, other: Position | tuple[int, ]):
        return self.__sub__(other)

    def get(self, index_: int) -> Any:
        """
        Get the value at the index, returning 0 if the index does not exist.
        """
        if index_ < 0 or not isinstance(index_, int):
            raise IndexError(f"Position index {index_} is out of range")

        try:
            return self[index_]
        except IndexError:
            return 0

    @classmethod
    def from_tuple(cls, tuple_: tuple) -> Position:
        """
        Construct a Position from a tuple.
        """
        return cls(*iter(tuple_))

    @classmethod
    def from_text(cls, text: str) -> Position:
        """
        Construct a Position from text, such as ``123,4``.
        """
        return cls.from_tuple(eval(f"({text})"))


def manhattan_distance(x: Position, y: Position) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


class Sensor:
    def __init__(self, position: Position, beacon: Position):
        self.position = position
        self.beacon = beacon
        self.radius = manhattan_distance(position, beacon)
        self.neighbours: list[Position] = []

    def __str__(self):
        return f"{self.position}, {self.radius}"

    @classmethod
    def from_text(cls, text: str) -> Sensor:
        sensor, beacon = text.split(":")
        sensor = sensor.replace("Sensor at x=", "").replace(" y=", "")
        beacon = beacon.replace(" closest beacon is at x=", "").replace(" y=", "")

        return cls(
            position=Position.from_text(sensor),
            beacon=Position.from_text(beacon),
        )

    @property
    def tuning_frequency(self):
        return (self.position[0] * 4_000_000) + self.position[1]

    def set_neighbours(self) -> None:
        def quadrant():
            for x in range(self.radius + 1):
                for y in range(self.radius + 1 - x):
                    yield Position(x, y)

        top_right = list(quadrant())
        top_left = [Position(-pos[0], pos[1]) for pos in top_right]
        bottom_right = [Position(pos[0], -pos[1]) for pos in top_right]
        bottom_left = [Position(-pos[0], -pos[1]) for pos in top_right]

        self.neighbours = [
            self.position + position
            for position in set(top_right + top_left + bottom_right + bottom_left)
        ]


class Sensors:
    def __init__(self, sensors: list[Sensor]):
        self.sensors = sensors

    def __str__(self):
        return f"Collection of {len(self.sensors)} sensors"

    def __iter__(self):
        yield from self.sensors

    def __getitem__(self, index: int):
        return self.sensors[index]

    @classmethod
    def from_text(cls, text: str) -> Sensors:
        return cls([
            Sensor.from_text(sensor)
            for sensor in text.split("\n")
        ])

    def set_neighbours(self) -> None:
        for sensor in self.sensors:
            sensor.set_neighbours()

    def _count_positions_with_no_beacons(self, y: int) -> int:
        positions = []
        beacons = []
        for sensor in self.sensors:
            # This is way too inefficient
            positions.extend(
                neighbour
                for neighbour in sensor.neighbours
                if neighbour[1] == y
            )
            beacons.append(sensor.beacon)

        return len({position for position in positions if position not in beacons})

    def count_positions_with_no_beacons(self, y: int) -> int:
        beacons = [sensor.beacon for sensor in self.sensors]
        min_sensor_x = min(sensor.position[0] for sensor in self.sensors)
        max_sensor_x = max(sensor.position[0] for sensor in self.sensors)
        min_sensor_radius = max(sensor.radius for sensor in self.sensors if sensor.position[0] == min_sensor_x)
        max_sensor_radius = max(sensor.radius for sensor in self.sensors if sensor.position[0] == max_sensor_x)

        positions = []
        for x in range(min_sensor_x - min_sensor_radius, max_sensor_x + max_sensor_radius + 1):
            position = Position(x, y)
            positions.extend(
                position
                for sensor in self.sensors
                if manhattan_distance(position, sensor.position) <= sensor.radius
            )

        return len({position for position in positions if position not in beacons})


# noinspection DuplicatedCode
# Math co-ordinates
UP = Position(0, 1)
DOWN = Position(0, -1)
LEFT = Position(-1, 0)
RIGHT = Position(1, 0)


def solution(input_: str) -> list[Any]:
    """
    Solve the day 15 problem!
    """
    sensors = Sensors.from_text(input_.strip())
    # sensors.set_neighbours()  # Takes way too long!

    return [
        sensors.count_positions_with_no_beacons(2_000_000),  # 10, 2_000_000
        0,
    ]
