"""
OOP solution for day 13.
"""
from __future__ import annotations
import collections.abc
import pprint
from typing import Any


def packify(value: Any) -> Packet:
    if value is None:
        return value
    elif isinstance(value, list):
        return Packet(value)
    elif isinstance(value, int):
        return value
    else:
        return value


class Packet(collections.abc.MutableSequence):
    """
    A packet, which is a list of integers or other packets.

    This inheritance implementation is based on the following:
    - https://github.com/python/cpython/blob/208a7e957b812ad3b3733791845447677a704f3e/Lib/collections/__init__.py#L1174
    """
    def __init__(self, items: Packet | list = None):
        """
        Create a Packet, which is a list of integers or other packets.
        """
        self.data = []
        if items is not None:
            if isinstance(items, Packet):
                self.data[:] = items.data[:]
            elif isinstance(items, int):
                self.data[:] = [items]
            else:
                self.data = list(items)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Packet(items={self.data})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i: int):
        return self.__class__(self.data[i]) if isinstance(i, slice) else self.data[i]

    def __setitem__(self, i: int, item: Any):
        self.data[i] = item

    def __delitem__(self, i: int):
        del self.data[i]

    def __eq__(self, other: Packet):
        return self.data == other.data

    def __lt__(self, other: Packet | int):
        """
        Compare 2 packets element-wise.

        TODO: Make this recursive, since we need to compare depths.
        """
        other = other if isinstance(other, Packet) else Packet(other)

        # sourcery skip: merge-duplicate-blocks, remove-redundant-if
        for i in range(max(len(self), len(other))):
            left, right = packify(self.get(i)), packify(other.get(i))
            print(f"Comparing {left} and {right} ({type(left)} and {type(right)})")
            if left is None and right is not None:
                # The left packet is smaller
                return True
            elif right is None:
                # The right packet is smaller
                return False
            elif left < right:
                # The left packet is smaller
                return True
            elif right < left:
                # The right packet is smaller
                return False

        return True

    def __le__(self, other: Packet):
        return self < other or self == other

    def __gt__(self, other: Packet):
        return not(self <= other)

    def __ge__(self, other: Packet):
        return self > other or self == other

    def insert(self, i: int, item: Any) -> None:
        """
        Insert an item at index i.
        """
        self.data.insert(i, item)

    def get(self, index_: int, default: Any = None) -> Any:
        """
        Get the value at the index, returning 0 if the index does not exist.
        """
        if index_ < 0 or not isinstance(index_, int):
            raise IndexError(f"Packet index {index_} is out of range")

        try:
            return self[index_]
        except IndexError:
            return default

    @classmethod
    def from_text(cls, text: str) -> Packet:
        """
        Convert the text representation into a packet.
        """
        return cls(list(eval(text)))


class PacketPair:
    """
    A pair of packets.
    """
    def __init__(self, left_packet: Packet, right_packet: Packet):
        self.left_packet = left_packet
        self.right_packet = right_packet

    def __str__(self):
        return f"<{self.left_packet}><{self.right_packet}>"

    def __repr__(self):
        return str(self)

    def __iter__(self):
        yield from [self.left_packet, self.right_packet]

    @classmethod
    def from_text(cls, text: str) -> PacketPair:
        """
        Parse a textual pair of packets into a PacketPair.
        """
        left, right = text.split("\n")
        return cls(Packet.from_text(left), Packet.from_text(right))


def solution(input_: str) -> list[Any]:
    """
    Solve the day 13 problem!
    """
    packet_pairs = {
        i: PacketPair.from_text(text)
        for i, text in enumerate(input_.strip().split("\n\n"))
    }
    # pprint.pprint(packet_pairs)

    for packet_pair in packet_pairs.values():
        packet_1, packet_2 = packet_pair
        print(packet_1, packet_2)
        print(packet_1 < packet_2, packet_1 > packet_2)

    quit()
    return [0, 0]
