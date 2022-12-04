"""
Day 2: Rock, Paper, Scissors!
"""
import functools

import advent_of_code.day_2.oop
import advent_of_code.day_2.optimal
import advent_of_code.utils


SAMPLE_INPUT = """
A Y
B X
C Z
"""


def read_input(use_sample: bool = True) -> str:
    """
    Open the day 2 input file and return its contents.

    https://adventofcode.com/2022/day/2/input
    """
    if use_sample:
        return SAMPLE_INPUT.strip()

    return advent_of_code.utils.read_input("day_2")


def solution(use_sample: bool = True, profile_solutions: bool = False) -> None:
    """
    Solve the day 2 problem!
    """
    input_ = read_input(use_sample=use_sample)

    print(advent_of_code.day_2.oop.solution(input_=input_))
    print(advent_of_code.day_2.optimal.solution(input_=input_))

    if profile_solutions:
        advent_of_code.utils.profile(
            oop_solution=functools.partial(
                advent_of_code.day_2.oop.solution,
                strategy_input=input_,
            ),
            optimal_solution=functools.partial(
                advent_of_code.day_2.optimal.solution,
                strategy_input=input_,
            ),
        )
