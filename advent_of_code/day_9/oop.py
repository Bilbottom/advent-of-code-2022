"""
OOP solution for day 9.
"""
from __future__ import annotations

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


class Knot:
    """
    A knot, which only has a position and its history.
    """
    def __init__(self, position: Position):
        self._position = position
        self.position_history = [position]

    def __str__(self):
        return str(self.position)

    def __repr__(self):
        return str(self.position)

    @property
    def position(self) -> Position:
        """
        The knot's position.
        """
        return self._position

    @position.setter
    def position(self, value: Position) -> None:
        """
        Set the knot's position.
        """
        self._position = value
        self.position_history.append(value)


class Rope:
    """
    A rope, whose head has a position and whose tail has a position.
    """
    def __init__(self, starting_position: Position, knots: int):
        """
        Create a rope with a starting position and some number of knots.
        """
        self.knots = knots
        self.knot_positions: dict[int, Knot] = {
            i: Knot(starting_position)
            for i in range(knots)
        }

    def __str__(self):
        return f"head={self.head_knot}, tail={self.tail_knot}"

    @property
    def head_knot(self) -> Knot:
        """
        The head's position.
        """
        return self.knot_positions[0]

    @property
    def tail_knot(self) -> Knot:
        """
        The tail's position.
        """
        return self.knot_positions[self.knots - 1]

    def resolve_knot_positions(self) -> None:
        """
        Update the knot positions to correctly follow the head around.
        """
        for key, knot in self.knot_positions.items():
            if key != 0:  # head
                self.knot_positions[key].position = resolve_knot_position(
                    upper_knot=self.knot_positions[key - 1].position,
                    lower_knot=knot.position,
                )

    def move(self, direction: str) -> None:
        """
        Move the head of the rope, and subsequently the tail of the rope if
        necessary.
        """
        self.knot_positions[0].position += DIRECTIONS[direction]
        self.resolve_knot_positions()

    def follow_instructions(self, instructions: list[str]) -> None:
        """
        Follow the instructions given, which are to move in different directions
        by various amounts.
        """
        for instruction in instructions:
            direction, quantity = instruction.split()
            for _ in range(int(quantity)):
                self.move(direction)


def resolve_knot_position(upper_knot: Position, lower_knot: Position) -> Position:
    """
    Update the lower knot's position to correctly follow the upper knot
    around.
    """
    x, y = (upper_knot - lower_knot)
    x_, y_ = abs(x), abs(y)
    if x_ == 2 and y_ == 2:
        return lower_knot + Position(x // x_, y // y_)
    elif x_ == 2:
        return lower_knot + Position(x // x_, y)
    elif y_ == 2:
        return lower_knot + Position(x, y // y_)
    elif x_ > 2 or y_ > 2:
        raise ValueError(f"Larger distance than expected, found {x, y=}")
    else:
        return lower_knot


# Math co-ordinates
UP = Position(0, 1)
DOWN = Position(0, -1)
LEFT = Position(-1, 0)
RIGHT = Position(1, 0)
DIRECTIONS = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT,
}


def solution(input_: str) -> list[Any]:
    """
    Solve the day 9 problem!
    """
    rope_1 = Rope(starting_position=Position(0, 0), knots=2)
    rope_1.follow_instructions(instructions=input_.strip().split("\n"))
    rope_2 = Rope(starting_position=Position(0, 0), knots=10)
    rope_2.follow_instructions(instructions=input_.strip().split("\n"))

    return [
        len(set(rope_1.tail_knot.position_history)),
        len(set(rope_2.tail_knot.position_history)),
    ]
