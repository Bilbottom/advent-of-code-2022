"""
Day 2: Rock, Paper, Scissors!
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

    with open("advent_of_code/day_3/input.csv", "r") as f:
        return f.read().strip()


def solution(profile_solutions: bool = False) -> None:
    """
    Solve the day 3 problem!
    """
    rucksack_input = read_input(use_sample=True)

    print(advent_of_code.day_3.oop.solution(rucksack_input=rucksack_input))
    print(advent_of_code.day_3.optimal.solution(rucksack_input=rucksack_input))

    if profile_solutions:
        advent_of_code.utils.profile(
            oop_solution=functools.partial(
                advent_of_code.day_3.oop.solution,
                rucksack_input=rucksack_input,
            ),
            optimal_solution=functools.partial(
                advent_of_code.day_3.optimal.solution,
                rucksack_input=rucksack_input,
            ),
        )
