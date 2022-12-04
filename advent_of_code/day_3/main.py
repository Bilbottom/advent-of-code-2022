"""
Day 3: Rucksack Reorganization!
"""
import functools

import advent_of_code.day_3.oop
import advent_of_code.day_3.optimal
import advent_of_code.utils


SAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def read_input(use_sample: bool = True) -> str:
    """
    Open the day 3 input file and return its contents.

    https://adventofcode.com/2022/day/3/input
    """
    if use_sample:
        return SAMPLE_INPUT.strip()

    return advent_of_code.utils.read_input("day_3")


def solution(use_sample: bool = True, profile_solutions: bool = False) -> None:
    """
    Solve the day 3 problem!
    """
    rucksack_input = read_input(use_sample=use_sample)

    print(advent_of_code.day_3.oop.solution(input_=rucksack_input))
    print(advent_of_code.day_3.optimal.solution(input_=rucksack_input))

    if profile_solutions:
        advent_of_code.utils.profile(
            oop_solution=functools.partial(
                advent_of_code.day_3.oop.solution,
                input_=rucksack_input,
            ),
            optimal_solution=functools.partial(
                advent_of_code.day_3.optimal.solution,
                input_=rucksack_input,
            ),
        )
