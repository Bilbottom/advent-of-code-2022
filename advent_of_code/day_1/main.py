"""
Day 1: Calorie Counting!
"""
import functools

import advent_of_code.day_1.oop
import advent_of_code.day_1.optimal
import profiler

USE_SAMPLE = False
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


def read_input() -> str:
    """
    Open the day 1 input file and return its contents.
    """
    with open("advent_of_code/day_1/day-1-input.csv", "r") as f:
        return f.read()


def profile(calorie_input: str) -> None:
    """
    Profile different solutions.
    """
    functions = {
        'oop': functools.partial(
            advent_of_code.day_1.oop.solution,
            calorie_input=calorie_input,
        ),
        'optimal': functools.partial(
            advent_of_code.day_1.optimal.solution,
            calorie_input=calorie_input,
        ),
    }
    profiler.time_functions(functions, 1_000)


def solution(profile_solutions: bool = False) -> None:
    """
    Solve the day 1 problem!
    """
    master_list_of_calories = SAMPLE_INPUT if USE_SAMPLE else read_input()

    print(advent_of_code.day_1.oop.solution(master_list_of_calories))
    print(advent_of_code.day_1.optimal.solution(master_list_of_calories))

    if profile_solutions:
        profile(master_list_of_calories)
