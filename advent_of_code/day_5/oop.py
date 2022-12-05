"""
OOP solution for day 5.
"""
from __future__ import annotations


class Stack:
    """
    A stack of items.

    A stack can be represented graphically in the following way::

        [D]
        [C]
        [M]

    This will be stored in a list, such as ``['M', 'C', 'D']``. The order is
    important: the bottom of the stack is on the left of the list (lowest index
    values), and the top of the stack is on the right of the list (highest index
    values).
    """
    def __init__(self, items: list[str]):
        self.items = items

    def __str__(self):
        return f"{self.items}"

    def __repr__(self):
        return f"Stack(items={self.items})"


class Stacks:
    """
    An ordered collection of Stack objects.

    Stacks can be represented graphically in the following way::

            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

    This will be stored in a dictionary where the keys are the stack number (the
    number underneath the stack in the representation above) and the values are
    the Stack objects.
    """
    def __init__(self, stacks: dict[Stack]):
        self.stacks = stacks

    def __str__(self):
        return f"{self.stacks}"

    @classmethod
    def from_string_repr(cls, stacks_text: str) -> Stacks:
        """

        """
        row_stacks = [
            [
                row[(4 * i) + 1: 4 * (i + 1) - 2]
                for i in range((len(row) + 1) // 4)
            ]
            for row in stacks_text.split("\n")
        ]
        items: dict[Stack] = {
            int(char[0]): Stack(items=[char[i] for i in range(1, 4) if char[i].strip() != ""])
            for char in zip(*row_stacks[::-1])
        }

        return cls(stacks=items)


class Instruction:
    def __init__(self, move_quantity: int, from_stack: int, to_stack: int):
        self.move_quantity = move_quantity
        self.from_stack = from_stack
        self.to_stack = to_stack


class Procedure:
    def __init__(self, procedure: list[Instruction]):
        self.procedure = procedure


def solution(input_: str) -> list[int]:
    """
    Solve the day 5 problem!
    """
    stacks, procedure = input_.split("\n\n")
    print(stacks, "\n\n")
    print(procedure)

    print(Stacks.from_string_repr(stacks))

    return [0, 0]
