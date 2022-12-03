"""
Advent of code 2022!

https://adventofcode.com/
"""
from typing import Protocol, Callable

import advent_of_code.day_1
import advent_of_code.day_2
import advent_of_code.day_3


class Solution(Protocol):
    oop_solution: Callable
    optimal_solution: Callable

    def read_input(self) -> str:
        ...

    def print_solution(self, use_sample: bool, profile_solutions: bool) -> str:
        ...


def main() -> None:
    """
    Print the solutions.
    """
    # advent_of_code.day_1.solution(use_sample=False, profile_solutions=False)
    # advent_of_code.day_2.solution(use_sample=False, profile_solutions=False)
    advent_of_code.day_3.solution(use_sample=False, profile_solutions=False)


if __name__ == "__main__":
    main()
