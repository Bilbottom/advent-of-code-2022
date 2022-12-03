"""
Optimal (?) solution for day 1.
"""
import bisect


def _sum_calories(list_of_calories: str) -> int:
    return sum(int(calories) for calories in list_of_calories.split("\n"))


def get_max_elf(list_of_calorie_lists: str) -> int:
    """
    Answer for part 1.
    """
    max_calories = 0
    for elf_list in list_of_calorie_lists.strip().split("\n\n"):
        max_calories = max(max_calories, _sum_calories(elf_list))

    return max_calories


def get_total_calories(list_of_calorie_lists: str) -> int:
    """
    Answer for part 2.
    """
    min_calories = 0
    top_calories = []
    for elf_list in list_of_calorie_lists.strip().split("\n\n"):
        calorie_sum = _sum_calories(elf_list)
        if len(top_calories) < 3:
            top_calories.append(calorie_sum)
            if len(top_calories) == 3:
                top_calories.sort()
                min_calories = min(top_calories)
        elif calorie_sum > min_calories:
            top_calories.pop(0)
            bisect.insort(top_calories, calorie_sum)
            min_calories = top_calories[0]

    return sum(top_calories)


def solution(input_: str) -> list[int]:
    """
    Solve the day 1 problem!
    """
    return [
        get_max_elf(input_),
        get_total_calories(input_),
    ]
