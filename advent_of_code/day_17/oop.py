"""
OOP solution for day 17.
"""
from __future__ import annotations

import abc
import itertools
from typing import Any, Type

from utils.geometry import Position

# noinspection DuplicatedCode
# Math co-ordinates
UP = Position(0, 1)
DOWN = Position(0, -1)
LEFT = Position(-1, 0)
RIGHT = Position(1, 0)


class Rock(abc.ABC):
    def __init__(self, top_left: Position):
        self.top_left = top_left
        self.height: int = 0
        self.width: int = 0
        self._shape: list[Position] = []

    @property
    def shape(self) -> set[Position]:
        return {self.top_left + position for position in self._shape}

    def move(self, direction: Position) -> None:
        self.top_left += direction

    def draw(self) -> None:
        image = ""
        for y in range(self.height):
            image += "\n"
            for x in range(self.width):
                image += "#" if Position(x, -y) in self._shape else "."

        print(image)


class Horizontal(Rock):
    def __init__(self, top_left: Position):
        super(Horizontal, self).__init__(top_left=top_left)
        self.height: int = 1
        self.width: int = 4
        self._shape: list[Position] = [
            Position(0, 0),
            Position(0, 0) + RIGHT,
            Position(0, 0) + (RIGHT * 2),
            Position(0, 0) + (RIGHT * 3),
        ]


class Plus(Rock):
    def __init__(self, top_left: Position):
        super(Plus, self).__init__(top_left=top_left)
        self.height: int = 3
        self.width: int = 3
        self._shape: list[Position] = [
            Position(0, 0) + RIGHT,
            Position(0, 0) + DOWN,
            Position(0, 0) + RIGHT + DOWN,
            Position(0, 0) + (RIGHT * 2) + DOWN,
            Position(0, 0) + RIGHT + (DOWN * 2),
        ]


class Bend(Rock):
    def __init__(self, top_left: Position):
        super(Bend, self).__init__(top_left=top_left)
        self.height: int = 3
        self.width: int = 3
        self._shape: list[Position] = [
            Position(0, 0) + (RIGHT * 2),
            Position(0, 0) + (RIGHT * 2) + DOWN,
            Position(0, 0) + (RIGHT * 2) + (DOWN * 2),
            Position(0, 0) + RIGHT + (DOWN * 2),
            Position(0, 0) + (DOWN * 2),
        ]


class Vertical(Rock):
    def __init__(self, top_left: Position):
        super(Vertical, self).__init__(top_left=top_left)
        self.height: int = 4
        self.width: int = 1
        self._shape: list[Position] = [
            Position(0, 0),
            Position(0, 0) + DOWN,
            Position(0, 0) + (DOWN * 2),
            Position(0, 0) + (DOWN * 3),
        ]


class Square(Rock):
    def __init__(self, top_left: Position):
        super(Square, self).__init__(top_left=top_left)
        self.height: int = 2
        self.width: int = 2
        self._shape: list[Position] = [
            Position(0, 0),
            Position(0, 0) + RIGHT,
            Position(0, 0) + DOWN,
            Position(0, 0) + RIGHT + DOWN,
        ]


class Chamber:
    def __init__(self, width: int):
        self.width = width


def intersection(shape_1: Rock, shape_2: Rock) -> bool:
    return shape_1.shape.intersection(shape_2.shape) != {}


ROCK_ORDER: dict[int, Type[Rock]] = {
    0: Horizontal,
    1: Plus,
    2: Bend,
    3: Vertical,
    4: Square,
}


def solution(input_: str) -> list[Any]:
    """
    Solve the day 17 problem!
    """
    print(input_.strip())

    chamber = Chamber(width=7)

    for shape in ROCK_ORDER.values():
        shape(Position(0, 0)).draw()

    quit()
    return [
        0,
        0,
    ]
