"""
OOP solution for day 2
"""
from __future__ import annotations

import enum

import advent_of_code.day_2.constants


class Hand(enum.Enum):
    """
    The played hand, either rock, paper, or scissors.

    This implements **non-transitive** comparisons so that ``hand_1 > hand_2``
    means that ``hand_1`` beats ``hand_2``, but ``hand_1 > hand_2 > hand_3``
    does not imply that ``hand_1 > hand_3``.
    """
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __eq__(self, other: Hand):
        return self.value == other.value

    def __gt__(self, other: Hand):
        return other.value == advent_of_code.day_2.constants.DEFEATS[self.value]

    def __ge__(self, other: Hand):
        return self > other or self == other

    def __lt__(self, other: Hand):
        return not(self >= other)

    def __le__(self, other: Hand):
        return self < other or self == other


class Round:
    """
    A round of rock, paper, scissors.

    Consists of 2 hands corresponding to the "player" and the "opponent". The
    round has a result and a score for the player.
    """
    def __init__(self, round_input: str):
        self._round = round_input
        self._opponent, self._player = round_input.split()

    def __repr__(self):
        return f"Round('{self._round}', {self.opponent=}, {self.player=}, {self.result=}, {self.score=})"

    @property
    def opponent(self) -> Hand:
        """
        The unencoded hand played by the opponent.
        """
        return Hand(advent_of_code.day_2.constants.ENCODING_OPPONENT[self._opponent])

    @property
    def player(self) -> Hand:
        """
        The unencoded hand played by the player.
        """
        return Hand(advent_of_code.day_2.constants.ENCODING_PLAYER_1[self._player])

    @property
    def result(self) -> str:
        """
        The player's result of this round.
        """
        if self.player > self.opponent:
            return "win"
        elif self.player == self.opponent:
            return "draw"
        elif self.player < self.opponent:
            return "lose"
        else:
            raise ValueError(f"Can't compare hands: {self.player=}, {self.opponent=}")

    @property
    def score(self) -> int:
        """
        The player's score from this round.
        """
        return sum([
            advent_of_code.day_2.constants.SCORES[self.player.value],
            advent_of_code.day_2.constants.SCORES[self.result],
        ])


class Strategy:
    """
    The strategy guide.
    """
    def __init__(self, strategy_input: str):
        self._strategy = strategy_input
        self.rounds = [Round(round_strategy) for round_strategy in strategy_input.split("\n")]

    def get_total_score(self) -> int:
        """
        Return the sum of the player's scores for each round.
        """
        return sum(rnd.score for rnd in self.rounds)


def solution(strategy_input: str) -> int:
    """
    Solve the day 2 problem!
    """
    strategy = Strategy(strategy_input)

    return strategy.get_total_score()
