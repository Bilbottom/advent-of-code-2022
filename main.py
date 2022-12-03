"""
Advent of code 2022!

https://adventofcode.com/

# TODO: Consider creating a Solution object with each day solution being a subclass?
"""
import advent_of_code.day_1
import advent_of_code.day_2
import advent_of_code.day_3


def main() -> None:
    """
    Print the solutions.
    """
    advent_of_code.day_1.solution(use_sample=False, profile_solutions=False)
    advent_of_code.day_2.solution(use_sample=False, profile_solutions=False)
    advent_of_code.day_3.solution(use_sample=False, profile_solutions=False)


if __name__ == "__main__":
    main()
