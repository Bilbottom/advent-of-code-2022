"""
OOP solution for day 16.
"""
from __future__ import annotations

import copy
import re
import time
from typing import Any


class Valve:
    def __init__(self, name: str, flow_rate: int):
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to: list[Valve] = []
        self.open = False

    def __str__(self):
        return f"<'{self.name}': {self.flow_rate} {self.open_icon}>"

    def __repr__(self):
        return self.__str__()

    def __deepcopy__(self, memo: dict = None):
        """
        Copied from:

        - https://stackoverflow.com/a/15774013/8213085
        """
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))

        return result

    @property
    def open_icon(self) -> str:
        return {
            True: "◉",
            False: "○",
        }[self.open]


class Valves:
    def __init__(self, valves: list[Valve], tunnels: dict[str, list[str]]):
        self.valves = valves
        self.tunnels = tunnels

        for valve in self.valves:
            valve.leads_to = [self[v] for v in self.tunnels[valve.name]]

    def __str__(self):
        return "[" + ", ".join(str(valve) for valve in self) + "]"

    def __iter__(self):
        yield from self.valves

    def __getitem__(self, item: str) -> Valve:
        for valve in self.valves:
            if valve.name == item:
                return valve

    def __deepcopy__(self, memo: dict = None):
        """
        Copied from:

        - https://stackoverflow.com/a/15774013/8213085
        """
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))

        return result

    @classmethod
    def from_text(cls, text: str) -> Valves:
        items = [
            re.sub(
                r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)$",
                repl=r"\1,\2,\3",
                string=line,
            ).split(",", 2)
            for line in text.split("\n")
        ]

        valves = [Valve(item[0], int(item[1])) for item in items]
        tunnels = {item[0]: item[2].split(", ") for item in items}

        return cls(valves=valves, tunnels=tunnels)


class Route:
    def __init__(self, valves: Valves):
        self.valves = valves
        self.current_valve = self.valves["AA"]
        self.current_pressure = 0
        self.open_valves = []

    def __str__(self):
        return f"'{self.current_valve.name}' {self.current_valve.open_icon}:" \
               f" {self.current_pressure} [{' '.join(v.name for v in self.open_valves)}]"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other: Route):
        return self.current_pressure < other.current_pressure

    def __le__(self, other: Route):
        return self.current_pressure <= other.current_pressure

    def __gt__(self, other: Route):
        return self.current_pressure > other.current_pressure

    def __ge__(self, other: Route):
        return self.current_pressure >= other.current_pressure

    def __deepcopy__(self, memo: dict = None):
        """
        Copied from:

        - https://stackoverflow.com/a/15774013/8213085
        """
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))

        return result

    @property
    def open_valve(self) -> bool:
        return self.current_valve.flow_rate > 0 and not self.current_valve.open

    @property
    def leads_to(self) -> list[Valve]:
        return self.current_valve.leads_to

    def _resolve_open_valves(self) -> None:
        for valve in self.open_valves:
            self.current_pressure += valve.flow_rate

    def _resolve_action(self, next_valve: Valve) -> None:
        # Open current valve
        if self.open_valve:
            print(f"Opening valve {self.current_valve}")
            self.current_valve.open = True
            self.open_valves.append(self.current_valve)
        # Travel to other valve
        else:
            self.current_valve = next_valve

    def run(self, next_valve: Valve | None) -> None:
        assert self.current_valve in self.open_valves if self.current_valve.open else True
        self._resolve_open_valves()
        self._resolve_action(next_valve)


class Cycles:
    def __init__(self, input_: str, total_time: int):
        self._input = input_
        self.total_time = total_time
        self.current_time = 0
        self.routes: list[Route] = [Route(Valves.from_text(input_))]

    def run(self):
        while self.current_time <= self.total_time:
            print(f"Running minute {1 + self.current_time} with {len(self.routes)} routes")

            extra_routes = []
            for route in self.routes.copy():
                if route.open_valve:
                    route.run(next_valve=None)
                else:
                    self.routes.remove(route)
                    for next_valve in route.leads_to:
                        new_route = copy.deepcopy(route)
                        new_route.run(next_valve=next_valve)
                        extra_routes.append(new_route)

            self.routes += extra_routes
            self.routes = sorted(self.routes)[-100:]
            self.current_time += 1

            print(self.routes)
            print()
            time.sleep(1)


def solution(input_: str) -> list[Any]:
    """
    Solve the day 16 problem!
    """
    print(input_)
    cycles = Cycles(input_=input_.strip(), total_time=30)
    cycles.run()

    quit()
    return [
        0,
        0,
    ]
