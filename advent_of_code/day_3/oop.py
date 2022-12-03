"""
OOP solution for day 3.
"""


class Rucksack:
    def __init__(self, contents: str):
        self.contents = contents

        print(contents.split("\n"))


def solution(rucksack_input: str) -> list[int]:
    """
    Solve the day 3 problem!
    """
    Rucksack(rucksack_input)

    return [
        0,
        0,
    ]
