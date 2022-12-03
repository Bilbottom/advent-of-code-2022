"""
Day 1: Calorie Counting!
"""
import functools

import advent_of_code.day_1.oop
import advent_of_code.day_1.optimal
import advent_of_code.utils


SAMPLE_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def read_input(use_sample: bool = True) -> str:
    """
    Open the day 1 input file and return its contents.

    https://adventofcode.com/2022/day/1/input
    """
    if use_sample:
        return SAMPLE_INPUT.strip()

    return advent_of_code.utils.read_input("day_1")


def solution(use_sample: bool = True, profile_solutions: bool = False) -> None:
    """
    Solve the day 1 problem!
    """
    calorie_input = read_input(use_sample=use_sample)

    print(advent_of_code.day_1.oop.solution(input_=calorie_input))
    print(advent_of_code.day_1.optimal.solution(input_=calorie_input))

    if profile_solutions:
        advent_of_code.utils.profile(
            oop_solution=functools.partial(
                advent_of_code.day_1.oop.solution,
                input_=calorie_input,
            ),
            optimal_solution=functools.partial(
                advent_of_code.day_1.optimal.solution,
                input_=calorie_input,
            ),
        )
