"""
Day 1: Calorie Counting!
"""
from __future__ import annotations

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


def _read_input() -> str:
    with open("advent_of_code/day_1/day-1-input.csv", "r") as f:
        return f.read()


class Elves:
    """
    Container for Elf objects.
    """
    def __init__(self):
        self.number_of_elves = 0
        self.largest_elf: Elf | None = None
        self.largest_elves: list[Elf] = []
        self._elves: list[Elf] = []

    def __getitem__(self, item):
        return self._elves[item]

    def _update_largest_elf(self, new_elf):
        if self.largest_elf is None:
            self.largest_elf = new_elf
        elif new_elf.calories > self.largest_elf.calories:
            self.largest_elf = new_elf

    def _update_largest_elves(self, new_elf):
        self.largest_elves.append(new_elf)
        if len(self.largest_elves) > 3:
            self.largest_elves.sort()
            self.largest_elves.pop(0)

    def add_elf(self, calorie_list: str) -> None:
        """
        Add an elf.

        If this elf has more calories than any previous elves, this elf will be
        saved.
        """
        new_elf = Elf(self.number_of_elves + 1, calorie_list)
        self._elves.append(new_elf)
        self.number_of_elves += 1
        self._update_largest_elf(new_elf)
        self._update_largest_elves(new_elf)


# sourcery skip: name-type-suffix
class Elf:
    """
    An elf, defined only by an ID and a list of calories.
    """
    def __init__(self, elf_id: int, calorie_list: str):
        self.id = elf_id
        self.calorie_list = calorie_list

    def __repr__(self):
        calorie_list = self.calorie_list.replace('\n', ',')
        return f"Elf(id={self.id}, calorie_list={calorie_list}, calories={self.calories})"

    def __lt__(self, other: Elf):
        return self.calories < other.calories

    def __gt__(self, other: Elf):
        return self.calories > other.calories

    def __add__(self, other: int):
        return self.calories + other

    def __radd__(self, other: int):
        return self.__add__(other)

    @property
    def calories(self) -> int:
        """
        The calories for the elf.

        Just the sum of calories in the list.
        """
        return sum(int(calories) for calories in self.calorie_list.split("\n"))


def get_max_elf(list_of_calorie_lists: str) -> Elf:
    """
    Answer for part 1.
    """
    elves = Elves()
    [elves.add_elf(elf_list) for elf_list in list_of_calorie_lists.strip().split("\n\n")]
    return elves.largest_elf


def get_total_calories(list_of_calorie_lists: str) -> int:
    """
    Answer for part 2.
    """
    elves = Elves()
    [elves.add_elf(elf_list) for elf_list in list_of_calorie_lists.strip().split("\n\n")]
    return sum(elves.largest_elves)


def solution() -> None:
    """
    Solve the day 1 problem!

    Note that this is solution aims to be OOP/Pythonic, not an optimal solution
    for time or space complexity.
    """
    master_list = SAMPLE_INPUT if USE_SAMPLE else _read_input()

    print(get_max_elf(master_list))
    print(get_total_calories(master_list))
