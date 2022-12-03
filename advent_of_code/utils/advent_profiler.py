"""
Profile the OOP and the optimal solutions.
"""
from typing import Callable

import profiler


def profile(oop_solution: Callable, optimal_solution: Callable) -> None:
    """
    Profile different solutions.
    """
    functions = {
        'oop': oop_solution,
        'optimal': optimal_solution,
    }
    profiler.time_functions(functions, 1_000)
