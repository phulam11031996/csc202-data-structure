from __future__ import annotations

from typing import Any, Optional


class Pair:

    def __init__(self, first: Any, rest: Optional[Pair]):
        self.first = first
        self.rest = rest

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Pair) and
            other.first == self.first and
            other.rest == self.rest
        )


# This defines the NumList type to be what was stated above:
# - None, or
# - Linked_list(first, rest)
LinkedList = Optional[Pair]


# no arguments -> None
def empty_list() -> None:
    """Returns an empty list."""
    return None


# LinkedList -> int
def length(my_list: LinkedList) -> int:
    """Returns the number of elements currently in the list."""
    if my_list is None:
        return 0

    return 1 + length(my_list.rest)


# LinkedList, int, value -> Linked_list
def add(my_list: LinkedList, index: int, value: Any) -> LinkedList:
    """Returns the resulting Linked_list."""
    if index < 0 or index > length(my_list):
        raise IndexError

    if index == 0:
        return Pair(value, my_list)

    return Pair(my_list.first, add(my_list.rest, index - 1, value))


# LinkedList, int -> Any
def get(my_list: LinkedList, index: int) -> Any:
    """Returns the value at the index positionin the list."""
    if (index < 0 or index >= length(my_list)):
        raise IndexError

    if index == 0:
        return my_list.first

    return get(my_list.rest, index - 1)


# LinkedList, int, value -> Linked_list
def setitem(my_list: LinkedList, index: int, value: Any) -> int:
    """Returns the resulting Linked_list."""
    if (index < 0 or index >= length(my_list)):
        raise IndexError

    if index == 0:
        return Pair(value, my_list.rest)

    return Pair(my_list.first, setitem(my_list.rest, index - 1, value))


# LinkedList, int -> LinkedList
def remove(my_list: LinkedList, index: int) -> tuple:
    """Returns a 2-tuple of, in this order, the element previously
    # at the specified index and the resulting list."""
    if index < 0 or index >= length(my_list):
        raise IndexError

    if index == 0:
        return (my_list.first, my_list.rest)

    if index > 0:
        remove_val, rest = remove(my_list.rest, index - 1)

    return (remove_val, Pair(my_list.first, rest))
