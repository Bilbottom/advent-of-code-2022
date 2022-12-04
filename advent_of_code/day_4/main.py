"""
Day 4: Camp Cleanup!
"""
import functools

import advent_of_code.day_4.oop
import advent_of_code.day_4.optimal
import advent_of_code.utils


SAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def read_input(use_sample: bool = True) -> str:
    """
    Open the day 4 input file and return its contents.

    https://adventofcode.com/2022/day/4/input
    """
    if use_sample:
        return SAMPLE_INPUT.strip()

    return advent_of_code.utils.read_input("day_4")


def solution(use_sample: bool = True, profile_solutions: bool = False) -> None:
    """
    Solve the day 4 problem!
    """
    input_ = read_input(use_sample=use_sample)

    print(advent_of_code.day_4.oop.solution(input_=input_))
    print(advent_of_code.day_4.optimal.solution(input_=input_))

    if profile_solutions:
        advent_of_code.utils.profile(
            oop_solution=functools.partial(
                advent_of_code.day_4.oop.solution,
                input_=input_,
            ),
            optimal_solution=functools.partial(
                advent_of_code.day_4.optimal.solution,
                input_=input_,
            ),
        )
