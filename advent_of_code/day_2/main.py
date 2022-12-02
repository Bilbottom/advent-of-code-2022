"""
Day 2: Rock, Paper, Scissors!
"""
import functools

import advent_of_code.day_2.oop
import advent_of_code.day_2.optimal
import profiler

USE_SAMPLE = False
SAMPLE_INPUT = """
A Y
B X
C Z
""".strip()


def read_input() -> str:
    """
    Open the day 1 input file and return its contents.

    https://adventofcode.com/2022/day/2/input
    """
    with open("advent_of_code/day_2/input.csv", "r") as f:
        return f.read().strip()


def profile(strategy_input: str) -> None:
    """
    Profile different solutions.
    """
    functions = {
        'oop': functools.partial(
            advent_of_code.day_2.oop.solution,
            calorie_input=strategy_input,
        ),
        'optimal': functools.partial(
            advent_of_code.day_2.optimal.solution,
            calorie_input=strategy_input,
        ),
    }
    profiler.time_functions(functions, 1_000)


def solution(profile_solutions: bool = False) -> None:
    """
    Solve the day 1 problem!
    """
    strategy_input = SAMPLE_INPUT if USE_SAMPLE else read_input()

    print(advent_of_code.day_2.oop.solution(strategy_input))
    print(advent_of_code.day_2.optimal.solution(strategy_input))

    if profile_solutions:
        profile(strategy_input)
