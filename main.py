"""
Advent of code 2022!

https://adventofcode.com/
"""
import advent_of_code.solutions
import advent_of_code.utils


def main() -> None:
    """
    Print the solutions.
    """
    # advent_of_code.utils.create_files(day=None)  # Default

    advent_of_code.solutions.print_all_solutions(
        print_all=False,
        use_sample=True,
        profile_solutions=False,
        repeat=10_000,
        print_day=11,
    )


if __name__ == "__main__":
    main()
