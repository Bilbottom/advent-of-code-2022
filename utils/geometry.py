"""
Classes representing objects from geometry.
"""
from __future__ import annotations

import itertools
from typing import Any


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
    """
    Calculate the Manhattan distance between 2 positions.
    """
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


class Area:
    def __init__(self, position_1: Position, position_2: Position):
        self.position_1 = position_1
        self.position_2 = position_2

    def __iter__(self):
        p1x, p1y = self.position_1
        p2x, p2y = self.position_2
        if p1x > p2x:
            p1x, p2x = p2x, p1x
        if p1y > p2y:
            p1y, p2y = p2y, p1y

        for y, x in itertools.product(range(1 + p2y - p1y), range(1 + p2x - p1x)):
            yield Position(p1x + x, p1y + y)
