"""
OOP solution for day 8.
"""
from typing import Any

import numpy as np


class Forest:
    def __init__(self, trees: str):
        self._trees = trees

    def __str__(self):
        return self._trees

    def get_forest(self) -> np.ndarray:
        return np.array(
            [int(tree) for tree in trees]
            for trees in self._trees.split("\n")
        )


def solution(input_: str) -> list[Any]:
    """
    Solve the day 8 problem!
    """
    forest = Forest(input_.strip())

    print(forest)
    print(forest.get_forest())

    forest2 = np.array(
        [int(tree) for tree in trees]
        for trees in input_.strip().split("\n")
    )
    print(forest2)
    print(np.array([[1, 2], [3, 4]]))

    quit()
    return [0, 0]
